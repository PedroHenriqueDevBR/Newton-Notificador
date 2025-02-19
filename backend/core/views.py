from typing import Any, Dict, List, Union

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, AbstractBaseUser, AnonymousUser
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.manager import BaseManager

from rest_framework import status  # type: ignore
from rest_framework.permissions import IsAuthenticated  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework.views import APIView  # type: ignore

from core.services.notificacor.notificador_service import NotificadorService
from core.utils.paginacao import LimitePaginacao
from core.serializers.notificacao_serializers import (
    NotificacaoSerializer,
    SistemaSerializer,
)
from core.models import Notificacao, StatusNotificacao


class IndexView(LoginRequiredMixin, View):
    permission_classes = [IsAuthenticated]

    def buscar_notificacoes_sistemas(
        self,
        selecionados: List[int],
        pagina: int,
        status: str | int,
    ):
        objetos = []
        if len(selecionados) == 0:
            objetos = Notificacao.objects.all().order_by("-id")
        else:
            sistemas: List[User] = []
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

    def formatar_sistemas_args(self, selecionados: list[int]):
        argumento = ""
        for selecionado in selecionados:
            argumento += f"&sistema={selecionado}"
        return argumento

    def formatar_status_args(self, status: str):
        return f"&status={status}" if status != "" else ""

    def get(self, request: HttpRequest):
        args = request.GET
        selecionados = args.getlist("sistema", None)
        pagina = int(request.GET.get("page", "1"))
        status = request.GET.get("status", "")
        selecionados = list(map(lambda pk: int(pk), selecionados))

        template_name = "index.html"
        context: Dict[str, Any] = {}
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


class NotificacoesApiView(APIView, LimitePaginacao):
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest):
        status_arg = request.GET.get("status", "")
        sistemas_arg = request.GET.getlist("sistema", [])
        notificacoes = self.carregar_notificacoes(
            status_arg=status_arg,
            sistemas_arg=sistemas_arg,
        )
        resultado: Any = self.paginate_queryset( # type: ignore
            notificacoes,
            request,
            view=self,
        )
        serializer = NotificacaoSerializer(resultado, many=True)
        return self.get_paginated_response(data=serializer.data) # type: ignore

    def carregar_notificacoes(
        self,
        status_arg: str = "",
        sistemas_arg: list[str] = [],
    ) -> BaseManager[Notificacao]:
        notificacoes = Notificacao.objects.all().order_by("-id")
        if status_arg != "":
            notificacoes = self.filtrar_status(
                notificacoes=notificacoes,
                status_arg=status_arg,
            )
        if len(sistemas_arg) != 0:
            notificacoes = self.filtrar_sistema(
                notificacoes=notificacoes,
                sistemas_arg=sistemas_arg,
            )
        return notificacoes

    def filtrar_sistema(
        self,
        notificacoes: BaseManager[Notificacao],
        sistemas_arg: list[str],
    ):
        sistemas = map(lambda sistema: int(sistema), sistemas_arg)
        return notificacoes.filter(sistema__id__in=sistemas)

    def filtrar_status(self, notificacoes: BaseManager[Notificacao], status_arg: str):
        if status_arg not in ["1", "2", "3", "4"]:
            return notificacoes

        status = int(status_arg)
        if status == StatusNotificacao.RECEBIDO:
            notificacoes = notificacoes.filter(
                status__status=StatusNotificacao.RECEBIDO
            ).exclude(
                Q(status__status=StatusNotificacao.ERRO)
                | Q(status__status=StatusNotificacao.ENVIADO)
                | Q(status__status=StatusNotificacao.CALLBACK),
            )
            return notificacoes
        if status == StatusNotificacao.ERRO:
            notificacoes = notificacoes.filter(
                Q(status__status=StatusNotificacao.ERRO)
            ).exclude(Q(status__status=StatusNotificacao.ENVIADO))
            return notificacoes
        if status == StatusNotificacao.ENVIADO:
            notificacoes = notificacoes.filter(
                Q(status__status=StatusNotificacao.ENVIADO)
            )
            return notificacoes
        return notificacoes


class DetalhesNotificacaoApiView(APIView, LimitePaginacao):
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest, pk: int):
        notificacao_query = Notificacao.objects.filter(pk=pk)
        if not notificacao_query.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        notificacao = notificacao_query[0]
        serializer = NotificacaoSerializer(notificacao)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


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
    ) -> Notificacao:
        notificacao = Notificacao.objects.create(
            destinatarios=destinatarios,
            assunto=assunto,
            conteudo=conteudo,
            sistema=sistema,
        )
        StatusNotificacao.objects.create(
            notificacao=notificacao,
            status=StatusNotificacao.RECEBIDO,
        )
        return notificacao

    def notificar(self, notificacao: Notificacao, service: NotificadorService):
        provedor_email = service.selecionar_provedor_email()
        service.notificar(
            notificacao=notificacao,
            provedor_email=provedor_email,
        )

    def post(self, request: HttpRequest):
        sistema = request.user
        dados: Dict[str, Any] = request.data  # type: ignore
        destinatarios: Any = dados.get("destinatarios", "")  # type: ignore
        assunto: Any = dados.get("assunto", "Assunto não definido")  # type: ignore
        conteudo: Any = dados.get("conteudo", "")  # type: ignore

        service = NotificadorService()
        provedor_email = service.selecionar_provedor_email()
        if provedor_email is None:
            return Response(
                data={"Erro": "Nenhum provedor de email configurado"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if self.dados_validos(destinatarios=destinatarios):
            notificacao = self.registrar_notificacao(
                sistema=sistema,
                destinatarios=destinatarios,
                assunto=assunto,
                conteudo=conteudo,
            )
            self.notificar(notificacao=notificacao, service=service)

            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def dados_validos(self, destinatarios: List[Any]) -> bool:
        if len(destinatarios) == 0:
            return False
        return True


class NotificarSMSApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest):
        return redirect("/")

    def registrar_notificacao(
        self,
        sistema: Union[AbstractBaseUser, AnonymousUser, User],
        destinatarios: str,
        assunto: str,
        conteudo: str,
    ) -> Notificacao:
        notificacao = Notificacao.objects.create(
            destinatarios=destinatarios,
            assunto=assunto,
            conteudo=conteudo,
            sistema=sistema,
        )
        StatusNotificacao.objects.create(
            notificacao=notificacao,
            status=StatusNotificacao.RECEBIDO,
        )
        return notificacao

    def post(self, request: HttpRequest):
        sistema = request.user
        dados: Dict[str, Any] = request.data  # type: ignore
        destinatario: Any = dados.get("destinatarios", "")  # type: ignore
        assunto: Any = dados.get("assunto", "Assunto não definido")  # type: ignore
        conteudo: Any = dados.get("conteudo", "")  # type: ignore

        service = NotificadorService()
        provedor_sms = service.selecionar_provedor_sms()
        if provedor_sms is None:
            return Response(
                data={"Erro": "Nenhum provedor de SMS configurado"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if self.dados_validos(destinatarios=destinatario):
            notificacao = self.registrar_notificacao(
                sistema=sistema,
                destinatarios=destinatario,
                assunto=assunto,
                conteudo=conteudo,
            )
            service.notificar(
                notificacao=notificacao,
                provedor_sms=provedor_sms,
            )

            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def dados_validos(self, destinatarios: List[Any]) -> bool:
        if len(destinatarios) == 0:
            return False
        return True


class NotificacaoInstataneaApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: HttpRequest):
        service = NotificadorService()
        provedor_email = service.selecionar_provedor_email()
        if provedor_email is None:
            return Response(
                data={"Erro": "Nenhum provedor de email configurado"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        dados = request.data  # type: ignore
        sistema_pk: int = dados.get("sistema", 0)  # type: ignore
        sistemas_query = User.objects.filter(pk=sistema_pk)
        if not sistemas_query.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        destinatarios: Any = dados.get("destinatarios", "")  # type: ignore
        assunto: Any = dados.get("assunto", "Assunto não definido")  # type: ignore
        conteudo: Any = dados.get("conteudo", "")  # type: ignore
        sistema: Any = sistemas_query[0]

        notificar_view = NotificarApiView()
        if notificar_view.dados_validos(destinatarios=destinatarios):
            notificacao = notificar_view.registrar_notificacao(
                sistema=sistema,
                destinatarios=destinatarios,
                assunto=assunto,
                conteudo=conteudo,
            )
            notificar_view.notificar(notificacao=notificacao, service=service)
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_401_UNAUTHORIZED)


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
