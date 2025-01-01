from django.urls import path
from app_mensajeria.views import enviar_mensaje, ver_mensajes

urlpatterns=[
    path("enviar-mensaje/", enviar_mensaje, name="enviar-mensaje"),
    path("ver-mensajes/", ver_mensajes, name="ver-mensajes"),
]