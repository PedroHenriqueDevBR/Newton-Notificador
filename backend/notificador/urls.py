from django.contrib import admin
from django.urls import path

from core.views import (ApresentarNotificacaoView, 
    IndexView, 
    NotificarApiView, 
    NotificacoesApiView, 
    SistemasApiView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("<int:pk>", ApresentarNotificacaoView.as_view(), name="apresentar"),
    path("api/v1/auth/token", TokenObtainPairView.as_view(), name="token"),
    path("api/v1/auth/refresh", TokenRefreshView.as_view(), name="refresh_token"),
    path("api/v1/notificar", NotificarApiView.as_view(), name="notificar"),
    path("api/v1/notificacoes", NotificacoesApiView.as_view(), name="notificacoes"),
    path("api/v1/sistemas", SistemasApiView.as_view(), name="sistemas"),
]
