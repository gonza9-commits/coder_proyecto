from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Curso, Profesor, Estudiante, Perfil, Tarea, Entregable
from .forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableForm, UserUpdateForm, UserProfileForm, TareaForm, EntregableForm

# Create your views here.


def ver_perfil(request):
   return render(request, "laApp/ver-perfil.html")


def editar_perfil(request):

   usuario = request.user

   profile, _ = Perfil.objects.get_or_create(user=usuario) 

   if request.method == "POST":
       user_form = UserUpdateForm(request.POST, instance=usuario)
       profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)

       if user_form.is_valid() and profile_form.is_valid():
           user_form.save()
           profile_form.save()
           return redirect("ver-perfil")
       else: 
           return redirect("inicio")

   else:
       user_form= UserUpdateForm(instance=usuario)
       profile_form = UserProfileForm(instance=profile)

   return render(request, "laApp/forms/editar-perfil.html", {"user_form":user_form, "profile_form": profile_form})



def cambiar_contraseña(request):

   usuario = request.user

   if request.method == "POST":
      form_contraseña = PasswordChangeForm(usuario, request.POST)
      if form_contraseña.is_valid():
         form_contraseña.save()
         update_session_auth_hash(request, usuario)
         return redirect("inicio")
      else:
         return redirect("inicio")

   else:
      form_contraseña = PasswordChangeForm(usuario) 

   return render(request, "laApp/forms/cambiar-contraseña.html", {"form_contraseña":form_contraseña})



def login_view(request):
   if request.method == "POST":
      username= request.POST.get("username")
      password= request.POST.get("password")
      user= authenticate(request, username=username, password=password)
      if user is not None: 
         login(request, user) 
         return redirect("inicio") 
      else: 
         return redirect("inicio")

   else:
      return render(request, "laApp/forms/login.html")
   
def tarea_list(request):
    tareas = Tarea.objects.all()
    return render(request, 'laApp/tareas.html', {'tarea': tareas})

def tarea_create(request):
    if request.method == 'POST':
        form = TareaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tarea')
    else:
        form = TareaForm()
    return render(request, 'laApp/forms/tarea-formulario.html', {'form': form})

def ver_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'laApp/ver-tareas.html', {'tareas': tareas})


def user_logout(request):
   logout(request)
   return redirect("login")

def register_view(request):
   if request.method == "POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("inicio")
   else:
       form= UserCreationForm()
   return render(request, "laApp/forms/register.html", {"form": form})




def inicio(request):
    return render(request, "laApp/index.html")

@login_required
def cursos(request):

    query= request.GET.get('q')

    if query:
       cursos= Curso.objects.filter(nombre__icontains=query) | Curso.objects.filter(comision__icontains=query)
    else: 
     cursos = Curso.objects.all()

    return render(request, "laApp/cursos.html", {"cursos":cursos})

@login_required
def profesores(request):
    query= request.GET.get('q')

    if query:
       profes= Profesor.objects.filter(nombre__icontains=query) 
    else: 
     profes = Profesor.objects.all()

    return render(request, "laApp/profesores.html", {"profes":profes})

def estudiantes(request):
    
   query= request.GET.get('q')

   if query:
       estudiantes= Estudiante.objects.filter(nombre__icontains=query) | Estudiante.objects.filter(comision__icontains=query)
   else: 
     estudiantes = Estudiante.objects.all()

   return render(request, "laApp/estudiantes.html", {"estudiantes":estudiantes})

   
def formulario_estudiante(request):

   if request.method == "POST":
       estudiante_form= EstudianteFormulario(request.POST)
       if estudiante_form.is_valid():
        estudiante_form.save()
       return redirect("estudiantes")
      
   else: 
      estudiante_form= EstudianteFormulario()
      return render(request, "laApp/forms/estudiante-formulario.html", {"form":estudiante_form})
    
def formulario_estudiante_api(request):

    if request.method == "POST":
       estudiante_form= EstudianteFormulario(request.POST)

       if estudiante_form.is_valid():
          info_limpia= estudiante_form.cleaned_data
          estudiante= Estudiante(nombre=info_limpia["nombre"], apellido=info_limpia["apellido"], email=info_limpia["email"] )
          estudiante.save()
          return redirect("estudiantes")

    else:
     estudiante_form= EstudianteFormulario()

    contexto= {"form":estudiante_form }

    return render(request, "laApp/forms/estudiante-formulario.html", contexto)
    

def entregable(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("entregable")
    else:
        form = EntregableForm()

    entregables = Entregable.objects.all()
    return render(request, 'laApp/entregable.html', {'form': form, 'entregables': entregables})

def ver_entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'laApp/ver-entregables.html', {'entregables': entregables})


def formulario_curso(request):

 if request.method == "POST":
    curso= Curso(nombre=request.POST["curso"], comision=request.POST["comision"] )
    curso.save()
    return redirect("cursos")
 else:
    return render(request, "laApp/forms/curso-formulario.html")
 
def formulario_curso_api(request):

    if request.method == "POST":
       curso_form= CursoFormulario(request.POST)

       if curso_form.is_valid():
          info_limpia= curso_form.cleaned_data
          curso= Curso(nombre=info_limpia["nombre"], comision=info_limpia["comision"] )
          curso.save()
          return redirect("cursos")

    else:
     curso_form= CursoFormulario()

    contexto= {"form":curso_form }

    return render(request, "laApp/forms/curso-formulario.html", contexto)

def info(request):
    return render(request, "laApp/info.html")


@login_required
def formulario_profe(request):

   if request.method == "POST":
       profe_form= ProfesorFormulario(request.POST)
       if profe_form.is_valid():
        profe_form.save()
       return redirect("profesores")
      
   else: 
      profe_form= ProfesorFormulario()
      return render(request, "laApp/forms/profe-formulario.html", {"form":profe_form})
    
def formulario_profe_api(request):

    if request.method == "POST":
       profe_form= ProfesorFormulario(request.POST)

       if profe_form.is_valid():
          info_limpia= profe_form.cleaned_data
          profe= Profesor(nombre=info_limpia["nombre"], apellido=info_limpia["apellido"], email=info_limpia["email"], profesion=info_limpia["profesion"] )
          profe.save()
          return redirect("profesores")

    else:
     profe_form= ProfesorFormulario()

    contexto= {"form":profe_form }

    return render(request, "laApp/forms/profe-formulario.html", contexto)
   
def eliminar_estudiante(request, id):

    estudiante= Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect("inicio")

def editar_estudiante(request, id):
   estudiante= Estudiante.objects.get(id=id)

   if request.method == "POST":
      estudiante_form= EstudianteFormulario(request.POST)
      if estudiante_form.is_valid():
         info_limpia = estudiante_form.cleaned_data
         estudiante.nombre= info_limpia["nombre"]
         estudiante.apellido= info_limpia["apellido"]
         estudiante.email= info_limpia["email"]
         estudiante.profesion= info_limpia["profesion"]
         estudiante.save()
      return redirect("profesores")
   
   else:
       estudiante_form= EstudianteFormulario(initial={"nombre":estudiante.nombre, "apellido":estudiante.apellido, "email":estudiante.email})

   return render(request, "laApp/editar-profe.html", {"form":estudiante_form})
   

def eliminar_profe(request, id):

    profesor= Profesor.objects.get(id=id)
    profesor.delete()
    return redirect("inicio")

def editar_profe(request, id):
   profesor= Profesor.objects.get(id=id)

   if request.method == "POST":
      profe_form= ProfesorFormulario(request.POST)
      if profe_form.is_valid():
         info_limpia = profe_form.cleaned_data
         profesor.nombre= info_limpia["nombre"]
         profesor.apellido= info_limpia["apellido"]
         profesor.email= info_limpia["email"]
         profesor.profesion= info_limpia["profesion"]
         profesor.save()
      return redirect("profesores")
   
   else:
       profe_form= ProfesorFormulario(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion": profesor.profesion})

   return render(request, "laApp/editar-profe.html", {"form":profe_form})
   

class CursoListView(ListView):
   model= Curso
   context_object_name = "cursos"
   template_name= "laApp/vbc/cursos-vbc.html"


class CursoCreateView(LoginRequiredMixin, CreateView):
   model= Curso
   template_name= "laApp/vbc/cursos-vbc-crear.html"
   fields= ["nombre", "comision"]
   success_url = reverse_lazy("cursos-vbc")

class CursoDeleteView(DeleteView):
   model= Curso
   template_name= "laApp/vbc/cursos-vbc-eliminar.html"
   success_url = reverse_lazy("cursos-vbc")

class CursoUpdateView(LoginRequiredMixin, UpdateView):
   model= Curso
   template_name= "laApp/vbc/cursos-vbc-editar.html"
   success_url = reverse_lazy("cursos-vbc")
   fields= "__all__"

class CursoDetailView(DetailView): 
   model= Curso
   template_name= "laApp/vbc/cursos-vbc-detalle.html"


