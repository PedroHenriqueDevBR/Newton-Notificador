from django.contrib import admin
from django.urls import path
from core.views import NotificarApiView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/notificar", NotificarApiView.as_view(), name="notificar"),
]
