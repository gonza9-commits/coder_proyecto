from django.urls import path
from laApp.views import inicio, cursos, profesores, estudiantes, entregables

urlpatterns = [
    path('inicio/', inicio),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
]