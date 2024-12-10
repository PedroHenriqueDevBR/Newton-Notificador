import smtplib
import email.utils
from email.message import EmailMessage
import ssl
from provedor.models import ProvedorEmail
from core.models import Notificacao, StatusNotificacao, DetalheErro


class PadraoMailBackend:
    def send_mail(
        self,
        provedor: ProvedorEmail,
        notificacao: Notificacao,
    ) -> bool:
        # Configuracao de provedor
        HOST = provedor.host
        PORT = provedor.numero_porta
        SENDERNAME = provedor.sender_name
        SENDER = provedor.sender_email
        USERNAME_SMTP = provedor.host_user
        password_smtp = provedor.host_password
        
        # Configuracao da notificacao
        RECIPIENT = notificacao.destinatarios
        SUBJECT = notificacao.assunto
        BODY_TEXT = notificacao.conteudo
        BODY_HTML = notificacao.conteudo

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
            return False
        else:
            StatusNotificacao.objects.create(
                notificacao=notificacao,
                status=StatusNotificacao.ENVIADO,
            )
            print("Notificacao enviada!")
            return True
