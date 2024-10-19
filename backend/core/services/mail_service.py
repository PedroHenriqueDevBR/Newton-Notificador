from django.conf import settings
import smtplib
import email.utils
from email.message import EmailMessage
import ssl
from core.models import Notificacao, StatusNotificacao, DetalheErro


class CustomMailBackend:
    def send_mail(
        self,
        subject: str,
        message: str,
        recipient_list: str,
        notificacao: Notificacao,
    ):
        SENDERNAME = "Não Responda"
        RECIPIENT = recipient_list
        SENDER = settings.DEFAULT_FROM_EMAIL
        USERNAME_SMTP = settings.EMAIL_HOST_USER
        password_smtp = settings.EMAIL_HOST_PASSWORD
        HOST = settings.EMAIL_HOST
        PORT = settings.EMAIL_PORT
        SUBJECT = subject

        BODY_TEXT = message
        BODY_HTML = message

        msg = EmailMessage()
        msg["Subject"] = SUBJECT
        msg["From"] = email.utils.formataddr((SENDERNAME, SENDER))
        msg["To"] = RECIPIENT

        msg.add_alternative(BODY_TEXT, subtype="text")
        msg.add_alternative(BODY_HTML, subtype="html")

        try:
            server = smtplib.SMTP(HOST, PORT)
            server.ehlo()
            server.starttls(
                context=ssl.create_default_context(
                    purpose=ssl.Purpose.SERVER_AUTH,
                    cafile=None,
                    capath=None,
                )
            )
            server.ehlo()
            server.login(USERNAME_SMTP, password_smtp)
            server.sendmail(SENDER, RECIPIENT, msg.as_string())
            server.close()
        except Exception as e:
            mensagem = f"{e}"
            status = StatusNotificacao.objects.create(
                notificacao=notificacao,
                status=StatusNotificacao.ERRO,
            )
            DetalheErro.objects.create(
                status=status,
                mensagem=mensagem,
            )
            print(mensagem)
        else:
            StatusNotificacao.objects.create(
                notificacao=notificacao,
                status=StatusNotificacao.ENVIADO,
            )
            print("Notificacao enviada!")


class MailService:

    def notificar(
        self,
        notificacao: Notificacao,
    ) -> None:
        mail_service = CustomMailBackend()
        mail_service.send_mail(
            subject=notificacao.assunto,
            message=notificacao.conteudo,
            recipient_list=notificacao.destinatarios,
            notificacao=notificacao,
        )
