from django.contrib import admin
from django.urls import path
from core.views import NotificarApiView, IndexView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("api/v1/notificar", NotificarApiView.as_view(), name="notificar"),
]
