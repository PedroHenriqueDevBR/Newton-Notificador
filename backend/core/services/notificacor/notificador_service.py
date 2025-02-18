from typing import Optional
from core.services.sms.twilio_sms import TwilioSMS
from core.services.email.padrao_email_service import PadraoMailBackend
from provedor.models import ProvedorEmail, ProvedorSMS
from core.models import Notificacao, NotificacaoEmail, NotificacaoSMS

class NotificadorService:

    def notificar(
        self,
        notificacao: Notificacao,
        provedor_email: Optional[ProvedorEmail] = None,
        provedor_sms: Optional[ProvedorSMS] = None,
    ) -> None:
        if provedor_email is not None:
            mail_service = PadraoMailBackend()
            if mail_service.send_mail(
                notificacao=notificacao,
                provedor=provedor_email,
            ):
                NotificacaoEmail.objects.create(
                    provedor=provedor_email,
                    notificacao=notificacao,
                )
        
        if provedor_sms is not None:
            sms_service = TwilioSMS(
                account_sid=provedor_sms.account_id,
                auth_token=provedor_sms.auth_token,
                remetente=provedor_sms.phone_number,
            )
            if sms_service.enviar_sms(
                para=notificacao.destinatarios,
                mensagem=notificacao.conteudo,
            ):
                NotificacaoSMS.objects.create(
                    provedor=provedor_sms,
                    notificacao=notificacao,
                )

    def selecionar_provedor_email(self):
        provedores = ProvedorEmail.objects.filter(
            ativo=True,
        ).order_by("prioridade")

        if not provedores.exists():
            return None
        return provedores[0]

    def selecionar_provedor_sms(self):
        provedores = ProvedorSMS.objects.filter(
            ativo=True,
        ).order_by("prioridade")

        if not provedores.exists():
            return None
        return provedores[0]