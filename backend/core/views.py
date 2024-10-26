import stat
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, AbstractBaseUser, AnonymousUser
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.manager import BaseManager
from typing import Union
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers.notificacao_serializers import NotificacaoSerializer, SistemaSerializer
from core.models import Notificacao, StatusNotificacao
from core.services.mail_service import MailService


class IndexView(LoginRequiredMixin, View):
    permission_classes = [IsAuthenticated]

    def buscar_notificacoes_sistemas(self, selecionados: list, pagina: int, status: str,):
        objetos = []
        if len(selecionados) == 0:
            objetos = Notificacao.objects.all().order_by("-id")
        else:
            sistemas = []
            for pk in selecionados:
                sistemas_query = User.objects.filter(pk=pk)
                if sistemas_query.exists():
                    sistemas.append(sistemas_query[0])

            objetos = Notificacao.objects.filter(
                sistema__in=sistemas,
            ).order_by("-id")

        if status != "" and status != "0":
            status_cast = int(status)
            objetos = objetos.filter(status__status=status_cast)

        if status == 1:
            objetos = objetos.exclude(
                Q(status__status=2) | Q(status__status=3),
            )

        paginator = Paginator(objetos, 20)
        return paginator.get_page(pagina)

    def formatar_sistemas_args(self, selecionados: list):
        argumento = ""
        for selecionado in selecionados:
            argumento += f"&sistema={selecionado}"
        return argumento

    def formatar_status_args(self, status):
        return f"&status={status}" if status != "" else ""

    def get(self, request: HttpRequest):
        args = request.GET
        selecionados = args.getlist("sistema", None)
        pagina = int(request.GET.get("page", '1'))
        status = request.GET.get("status", "")
        selecionados = list(map(lambda pk: int(pk), selecionados))

        template_name = "index.html"
        context = {}
        context["notificacoes"] = self.buscar_notificacoes_sistemas(
            selecionados=selecionados, pagina=pagina, status=status
        )
        context["sistemas"] = User.objects.filter(
            is_staff=False,
            is_superuser=False,
        )
        context["sistemas_args"] = self.formatar_sistemas_args(
            selecionados=selecionados,
        )
        context["status_args"] = self.formatar_status_args(
            status=status,
        )
        context["selecionados"] = selecionados
        return render(request, template_name, context)


class NotificacoesApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest):
        status_arg = request.GET.get('status', '')
        notificacoes = self.carregar_notificacoes(status_arg=status_arg)
        serializer = NotificacaoSerializer(notificacoes, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def carregar_notificacoes(self, status_arg: str = '',) -> BaseManager[Notificacao]:
        notificacoes = Notificacao.objects.all()
        if status_arg == '':
            return notificacoes
        notificacoes = self.filtrar_status(notificacoes=notificacoes, status_arg=status_arg,)
        return notificacoes
        
    
    def filtrar_status(self, notificacoes: BaseManager[Notificacao], status_arg: str):
        if status_arg not in ['1','2','3','4']:
            return notificacoes
        
        status = int(status_arg)
        if status == StatusNotificacao.RECEBIDO:
            notificacoes = notificacoes.filter(
                status__status=StatusNotificacao.RECEBIDO
            ).exclude(
                Q(status__status=StatusNotificacao.ERRO) | 
                Q(status__status=StatusNotificacao.ENVIADO) | 
                Q(status__status=StatusNotificacao.CALLBACK),
            )
            return notificacoes
        if status == StatusNotificacao.ERRO:
            notificacoes = notificacoes.filter(Q(status__status=StatusNotificacao.ERRO)).exclude(Q(status__status=StatusNotificacao.ENVIADO))
            return notificacoes
        if status == StatusNotificacao.ENVIADO:
            notificacoes = notificacoes.filter(Q(status__status=StatusNotificacao.ENVIADO))
            return notificacoes
        return notificacoes
    

class SistemasApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest):
        sistemas = User.objects.filter(
            is_staff=False,
            is_superuser=False,
        )
        serializer = SistemaSerializer(sistemas, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class NotificarApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest):
        return redirect("/")

    def registrar_notificacao(
        self,
        sistema: Union[AbstractBaseUser, AnonymousUser, User],
        destinatarios: str,
        assunto: str,
        conteudo: str,
        eh_html: bool,
    ) -> Notificacao:        
        notificacao = Notificacao.objects.create(
            destinatarios=destinatarios,
            assunto=assunto,
            conteudo=conteudo,
            eh_html=eh_html,
            sistema=sistema,
        )
        StatusNotificacao.objects.create(
            notificacao=notificacao,
            status=StatusNotificacao.RECEBIDO,
        )
        return notificacao

    def post(self, request: HttpRequest):
        sistema = request.user
        dados = request.data # type: ignore
        destinatarios = dados.get("destinatarios", "")
        assunto = dados.get("assunto", "Assunto não definido")
        conteudo = dados.get("conteudo", "")
        eh_html = dados.get("eh_html", False)

        if self.dados_validos(destinatarios=destinatarios):
            service = MailService()
            notificacao = self.registrar_notificacao(
                sistema=sistema,
                destinatarios=destinatarios,
                assunto=assunto,
                conteudo=conteudo,
                eh_html=eh_html,
            )
            service.notificar(notificacao=notificacao)

            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        # try:
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

    def dados_validos(self, destinatarios):
        if len(destinatarios) == 0:
            return False
        return True


class ApresentarNotificacaoView(LoginRequiredMixin, View):
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest, pk: int):
        notificacoes_query = Notificacao.objects.filter(pk=pk)  #  type: ignore
        if not notificacoes_query.exists():
            return redirect("index")

        notificacao = notificacoes_query.first()
        template_name = "detalhes.html"
        context = {"notificacao": notificacao}
        return render(request, template_name, context)
