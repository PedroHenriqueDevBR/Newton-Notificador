from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from core.models import Notificacao, StatusNotificacao
from core.services.mail_service import MailService


class NotificarApiView(APIView):
    name = "NotificarApiView"
    permission_classes = [IsAuthenticated]

    def registrar_notificacao(
        self,
        sistema,
        destinatarios,
        assunto,
        conteudo,
        eh_html,
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
