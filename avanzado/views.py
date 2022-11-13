from django.shortcuts import redirect, render
from avanzado.models import Mascota, Auto
from avanzado.forms import MascotaFormulario, BusquedaAuto
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def ver_mascotas(request):
    
    mascotas = Mascota.objects.all()
    
    return render(request, 'avanzado/ver_mascotas.html', {'mascotas': mascotas})
@login_required
def crear_mascota(request):
    
    if request.method =='POST':
        formulario = MascotaFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            mascota = Mascota(nombre=datos['nombre'], tipo=datos['tipo'], edad=datos['edad'], fecha_nacimiento=datos['fecha_nacimiento'])
            mascota.save()
            return redirect('ver_mascotas')
        else:
            return render(request, 'avanzado/crear_mascota.html', {'formulario': formulario})    
    formulario = MascotaFormulario()
    
    return render(request, 'avanzado/crear_mascota.html', {'formulario': formulario})
@login_required
def editar_mascota(request, id):
    
    mascota = Mascota.objects.get(id=id)
    
    if request.method =='POST':
        formulario = MascotaFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
                    
            mascota.nombre = datos['nombre']
            mascota.tipo = datos['tipo']
            mascota.edad = datos['edad']
            mascota.fecha_nacimiento = datos['fecha_nacimiento']
            
            mascota.save()
            return redirect('ver_mascotas')
        else:
            return render(request, 'avanzado/editar_mascota.html', {'formulario': formulario})
            
    formulario = MascotaFormulario(initial={'nombre': mascota.nombre,'tipo': mascota.tipo,'edad':mascota.edad,'fecha_nacimiento':mascota.fecha_nacimiento})
    
    return render(request, 'avanzado/editar_mascota.html', {'formulario': formulario, 'mascota':mascota})
@login_required
def eliminar_mascota(request, id):
    
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('ver_mascotas')

class ListaAutos(ListView):
    model = Auto
    template_name = "avanzado/ver_autos.html"
    
    def get_queryset(self):
        chasis = self.request.GET.get('chasis', '')
        if chasis:
            object_list = self.model.objects.filter(chasis__icontains=chasis)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaAuto()
        return context
    
class EditarAuto(LoginRequiredMixin, UpdateView):
    model = Auto
    success_url = '/avanzado/autos/'
    template_name = 'avanzado/editar_auto.html'
    fields = ['modelo', 'marca', 'cant_puertas', 'color', 'chasis', 'descripcion']
    
class CrearAuto(LoginRequiredMixin, CreateView):
    model = Auto
    success_url = '/avanzado/autos/'
    template_name = 'avanzado/crear_auto.html'
    fields = ['modelo', 'marca', 'cant_puertas', 'color', 'chasis', 'descripcion']


class EliminarAuto(LoginRequiredMixin, DeleteView):
    model = Auto
    success_url = '/avanzado/autos/'
    template_name = 'avanzado/eliminar_auto.html'
    
class VerAuto(DetailView):
    model = Auto
    template_name = 'avanzado/ver_auto.html'