from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render
import random

from home.models import familiar

def hola(request):
    return HttpResponse('Buenos dias mi Chiclita')

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
#     cargar_archivo = open(r'C:\Users\UNUMBIO\Documents\Mi Código\Nueva Practica\Django\templates\tu_template.html', 'r')
    
#     template = Template(cargar_archivo.read())
#     cargar_archivo.close()
#     contexto = Context({'persona': nombre})
#     template_renderizado = template.render(contexto)
# Para configurar dónde se buscan los archivos, en settings, DIR, se copia r'dirección
# de la carpeta templates'
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

def crear_familiar(request, nombre, apellido):
    
    persona = familiar(nombre=nombre, apellido=apellido, edad=random.randrange(1, 99), fecha_nacimiento=datetime.now())
    persona.save()
    
    # template = loader.get_template('crear_familiar.html')
    # template_renderizado = template.render({'familiar': persona})
    
    # return HttpResponse(template_renderizado)
    return render(request, 'home/crear_familiar.html', {'familiar': persona})

def ver_familiares(request):
    
    familiares = familiar.objects.all()
    # template = loader.get_template('ver_familiares.html')
    # template_renderizado = template.render({'familiares': familiares})
    
    # return HttpResponse(template_renderizado)
    
    return render(request, 'home/ver_familiares.html', {'familiares': familiares})

def index(request):
    
    return render(request, 'home/index.html')