from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Notificacao(models.Model):
    destinatarios = models.CharField(max_length=1500)
    assunto = models.CharField(max_length=2500)
    conteudo = models.TextField(max_length=5000)
    eh_html = models.BooleanField(default=False)
    sistema = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.assunto}"

    class Meta:
        verbose_name = "Notificacao"
        verbose_name_plural = "Notificacoes"


class StatusNotificacao(models.Model):
    RECEBIDO = 1
    ENVIADO = 2
    ERRO = 3
    CALLBACK = 4

    STATUS = [
        (RECEBIDO, "Recebido"),
        (ENVIADO, "Enviado"),
        (ERRO, "Erro"),
        (CALLBACK, "Callback"),
    ]

    registrado_em = models.DateTimeField()
    status = models.IntegerField(
        choices=STATUS,
        null=True,
        blank=True,
    )
    notificacao = models.ForeignKey(
        Notificacao,
        on_delete=models.CASCADE,
        related_name="status",
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.registrado_em = timezone.now()
        return super(StatusNotificacao, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.notificacao} -> {self.status}"

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"
