from django.contrib import admin
from .models import Notificacao, StatusNotificacao


@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = (
        "destinatarios",
        "assunto",
        "conteudo",
        "eh_html",
        "sistema",
    )


@admin.register(StatusNotificacao)
class StatusNotificacaoAdmin(admin.ModelAdmin):
    list_display = (
        "registrado_em",
        "status",
        "notificacao",
    )
