from django.contrib import admin
from .models import ProvedorEmail, ProvedorSMS


@admin.register(ProvedorEmail)
class ProvedorEmailAdmin(admin.ModelAdmin):
    list_display = (
        "opcao",
        "prioridade",
        "ativo",
        "host",
        "port",
        "sender_name",
        "sender_email",
        "host_user",
        "host_password",
        "use_tls",
    )


@admin.register(ProvedorSMS)
class ProvedorSMSAdmin(admin.ModelAdmin):
    list_display = (
        "opcao",
        "prioridade",
        "ativo",
        "account_id",
        "auth_token",
        "phone_number",
    )
