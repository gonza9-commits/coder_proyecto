from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "laApp/index.html")

def cursos(request):
    return render(request, "laApp/cursos.html")

def profesores(request):
    return HttpResponse("vista de profesores")

def estudiantes(request):
    return HttpResponse("vista de estudiantes")

def entregables(request):
    return HttpResponse("vista de entregables")



