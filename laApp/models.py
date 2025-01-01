from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    descripcion= models.TextField(null=True)
    
    def __str__(self):
        return f"Nombre del curso: {self.nombre} - Numero de comision: {self.comision}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre del profesor: {self.nombre} - Numero de comision: {self.apellido}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_Entrega = models.DateField(auto_now_add=True)
    texto = models.TextField(null=True)
    entregado = models.BooleanField(default=False)

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profile_picture/", null= True, blank= True)

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='tareas/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
