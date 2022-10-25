from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random
from home.forms import BusquedaFamiliarFormulario, FamiliarFormulario

from home.models import familiar

def hola(request):
    return HttpResponse('<h1>Buenos dias mi Chiclita</h1>')

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_y_hora}')

def calcular_fecha_nacimiento(request, edad):
    
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} sería: {fecha}')

def mi_template(request):
    cargar_archivo = open(r'C:\Users\UNUMBIO\Documents\Mi Código\Nueva Practica\Django\home\templates\mi_template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):    

    template = loader.get_template('home/tu_template.html')
    template_renderizado = template.render({'persona': nombre})
    
    return HttpResponse(template_renderizado)

def prueba_template(request):
    
    mi_contexto = {
        'rango' : list(range(1,11)),
        'valor_aleatorio': random.randrange(1,11)
        }
    
    template = loader.get_template('home/prueba_template.html')
    template_renderizado = template.render(mi_contexto)
    
    return HttpResponse(template_renderizado)

def crear_familiar(request):
    if request.method == 'POST':
        
        formulario = FamiliarFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_creacion = data.get('fecha_creacion', datetime.now())
            
            persona = familiar(nombre=nombre, apellido=apellido, edad=edad, fecha_creacion=fecha_creacion)
            persona.save()
        
        return redirect('ver_familiares')
    
    formulario = FamiliarFormulario()
   
    return render(request, 'home/crear_familiar.html', {'formulario': formulario})

def ver_familiares(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        familiares = familiar.objects.filter(nombre__icontains=nombre)
    else:
        familiares = familiar.objects.all()
    
    formulario = BusquedaFamiliarFormulario()

    return render(request, 'home/ver_familiares.html', {'familiares': familiares,'formulario': formulario})

def index(request):
    
    return render(request, 'home/index.html')