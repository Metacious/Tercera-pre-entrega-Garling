from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

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

# Formularios de usuarios

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password1 = forms.CharField(label = 'Repetir Contraseña', widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
