from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profesor, Curso, Estudiante, Perfil, Tarea, Entregable

class CursoFormulario(forms.ModelForm):
    class Meta:
        model= Curso
        fields= "__all__"
        widgets= {
            "nombre": forms.TextInput(attrs={
                "placeholder":"Ingrese el nombre del curso"
            }),
            "comision": forms.NumberInput(attrs={
                "placeholder":"Ingrese el numero de comisión"
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder":"Ingrese una descripción"
            })
        }
     


class EstudianteFormulario(forms.ModelForm):

    class Meta:
        model= Estudiante
        fields= ["nombre", "apellido", "email"]

class ProfesorFormulario(forms.ModelForm):

    class Meta:
        model= Profesor
        fields= ["nombre", "apellido", "email", "profesion"]


class UserUpdateForm(forms.ModelForm):

    class Meta: 
        model= User
        fields=("first_name", "last_name", "email")

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ["photo"]

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ('titulo', 'descripcion', 'archivo')

class EntregableForm(forms.ModelForm):
     class Meta:
        model = Entregable
        fields = ('nombre', 'texto')