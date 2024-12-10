from twilio.rest import Client


class TwilioSMS:

    def __init__(
        self,
        account_sid: str,
        auth_token: str,
        remetente: str,
    ) -> None:
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.remetente = remetente
        self.client = Client(account_sid, auth_token)

    def enviar_sms(self, para: str, mensagem: str) -> bool:
        try:
            response = self.client.messages.create(
                from_=self.remetente,
                to=para,
                body=mensagem,
            )
            print("SMS enviado -> " + str(response.sid))
            return True
        except:
            return False
