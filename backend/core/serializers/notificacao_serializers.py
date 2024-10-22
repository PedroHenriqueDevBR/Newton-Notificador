from rest_framework import serializers
from core.models import Notificacao, StatusNotificacao
from django.contrib.auth.models import User


class SistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "is_active",
            "is_superuser",
        ]


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusNotificacao
        fields = [
            "id",
            "registrado_em",
            "status",
        ]


class NotificacaoSerializer(serializers.ModelSerializer):
    status = StatusSerializer(many=True)
    sistema = SistemaSerializer(many=False)
    class Meta:
        model = Notificacao
        depth = 1
        fields = [
            "id",
            "destinatarios",
            "assunto",
            "conteudo",
            "eh_html",
            "sistema",
            "status"
        ]