from django.contrib import admin
from .models import Notificacao, StatusNotificacao, DetalheErro


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


@admin.register(DetalheErro)
class DetalheErroAdmin(admin.ModelAdmin):
    list_display = (
        "status",
        "mensagem",
    )
