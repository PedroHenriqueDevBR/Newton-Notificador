from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from core.models import Notificacao, StatusNotificacao
from core.services.mail_service import MailService
from django.views.generic import View
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, View):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        template_name = "index.html"
        context = {
            "notificacoes": Notificacao.objects.all().order_by("-id"),
        }
        return render(request, template_name, context)


class NotificarApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return redirect("/")

    def registrar_notificacao(
        self,
        sistema: User,
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

    def post(self, request):
        sistema = request.user
        dados = request.data
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
