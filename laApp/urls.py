from django.urls import path
from laApp import views

urlpatterns = [
    path('', views.inicio, name="inicio"),

    path('info/', views.info, name="info"),

    path('tareas/', views.tarea_list, name='tarea'),
    path('crear-tarea/', views.tarea_create, name='crear-tarea'),
    path('ver-tareas/', views.ver_tareas, name='ver-tareas'),

    path('ver-perfil/', views.ver_perfil, name="ver-perfil"),
    path('editar-perfil/', views.editar_perfil, name="editar-perfil"),
    path('cambiar-contraseña/', views.cambiar_contraseña, name="cambiar-contraseña"),

    path('login/', views.login_view, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.register_view, name="register"),

    path('cursos/', views.cursos, name="cursos"),
    path('profesores/', views.profesores, name="profesores"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('entregable/', views.entregable, name="entregable"),
    path('ver-entregables/', views.ver_entregables, name='ver-entregables'),
    path('curso-formulario/', views.formulario_curso_api, name="curso-formulario"),
    path('profe-formulario/', views.formulario_profe_api, name="profe-formulario"),
    path('estudiante-formulario/', views.formulario_estudiante_api, name="estudiante-formulario"),
    # path('profe-formulario/', views.formulario_profe, name="profe-formulario"),
    # path('estudiante-formulario/', views.formulario_estudiante, name="estudiante-formulario"),
    path('profe-eliminar/<int:id>', views.eliminar_profe, name="profe-eliminar"),
    path('profe-editar/<int:id>', views.editar_profe, name="profe-editar"),
    path('editar-estudiante/<int:id>', views.editar_estudiante, name="editar-estudiante"),
    path('eliminar-estudiante/<int:id>', views.eliminar_estudiante, name="eliminar-estudiante"),


    path('cursos-vbc', views.CursoListView.as_view(), name="cursos-vbc"),
    path('cursos-vbc-crear', views.CursoCreateView.as_view(), name="cursos-vbc-crear"),
    path('cursos-vbc-eliminar/<int:pk>', views.CursoDeleteView.as_view(), name="cursos-vbc-eliminar"),
    path('cursos-vbc-editar/<int:pk>', views.CursoUpdateView.as_view(), name="cursos-vbc-editar"),
    path('cursos-vbc-detalle/<int:pk>', views.CursoDetailView.as_view(), name="cursos-vbc-detalle"),
]