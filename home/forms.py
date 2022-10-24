from django import forms
from django.forms import DateField, IntegerField

class FamiliarFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)