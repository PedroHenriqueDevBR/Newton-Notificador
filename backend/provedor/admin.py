from django.contrib import admin
from .models import ProvedorEmail, ProvedorSMS


@admin.register(ProvedorEmail)
class ProvedorEmailAdmin(admin.ModelAdmin):
    list_display = (
        "provedor",
        "prioridade",
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
        "provedor",
        "prioridade",
        "account_id",
        "auth_token",
        "phone_number",
    )
