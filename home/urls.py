from django.urls import path

from home import views


urlpatterns = [
    path('', views.index, name='index'),
    path('hola/', views.hola, name='hola'),
    path('fecha/', views.fecha, name='fecha'),
    path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento),
    # path('mi-template/', views.mi_template, name='mi_template'),
    path('mi-template/<str:nombre>', views.tu_template),
    path('prueba-template/', views.prueba_template),
    path('ver-familiares/', views.ver_familiares, name='ver_familiares'),
    path('crear-familiar/', views.crear_familiar, name='crear_familiar'),
]
