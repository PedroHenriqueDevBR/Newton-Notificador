from django.db import models

class Provedor(models.Model):
    PADRAO = 1
    TWILIO = 2

    PROVEDORES = (
        (PADRAO, 'Padrao'),
        (TWILIO, "Twilio"),
    )

    provedor = models.IntegerField(choices=PROVEDORES, default=TWILIO)
    prioridade = models.IntegerField(default=0)

    class Meta:
        abstract = True


class ProvedorSMS(Provedor):
    account_id = models.CharField(max_length=250)
    auth_token = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"${self.provedor} -> ${self.phone_number}"


class ProvedorEmail(Provedor):
    host = models.CharField(max_length=500)
    port = models.CharField(max_length=10)
    sender_name = models.CharField(max_length=250)
    sender_email = models.CharField(max_length=250)
    host_user = models.CharField(max_length=250)
    host_password = models.CharField(max_length=250)
    use_tls = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"${self.provedor} -> ${self.host}"
