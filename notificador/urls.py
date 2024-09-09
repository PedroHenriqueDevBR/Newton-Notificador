from django.contrib import admin
from django.urls import path

from core.views import ApresentarNotificacaoView, IndexView, NotificarApiView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("/<int:pk>", ApresentarNotificacaoView.as_view(), name="apresentar"),
    path("api/v1/notificar", NotificarApiView.as_view(), name="notificar"),
]
