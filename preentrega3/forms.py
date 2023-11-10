from django import forms

class HeroeFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=32)
    tipo = forms.CharField(required=True, max_length=16)
    aporte = forms.CharField(required=True, max_length=16)
    vida = forms.IntegerField(required=True) 
    velocidad = forms.IntegerField(required=True)

class ArmaFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=32)
    rareza = forms.CharField(required=True, max_length=16)
    descripcion = forms.CharField(required=True, max_length=256)
    costo = forms.IntegerField(required=True)

class ConsumibleFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=32)
    rareza = forms.CharField(required=True, max_length=16)
    descripcion = forms.CharField(required=True, max_length=256)
    sanacion = forms.IntegerField(required=True)
    duracion = forms.IntegerField(required=True)
    costo = forms.IntegerField(required=True)