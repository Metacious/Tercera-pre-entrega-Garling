from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Heroe, Arma, Consumible

# Página de inicio
def dota(request):
    # Creamos contexto para trabajar con parámetros.
    context = {}

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= loader.get_template('index.html'),
        context= context                                                                                                                                                                                                
    )
    # Devuelve la variable http_response
    return http_response

# Vistas de formularios
def formulario_heroes(request):
        # Creamos contexto para trabajar con parámetros.
    context = {}

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= 'formulario-heroes.html',
        context= context
    )
    # Devuelve la variable http_response
    return http_response

def formulario_armas(request):
        # Creamos contexto para trabajar con parámetros.
    context = {}

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= 'formulario-armas.html',
        context= context
    )
    # Devuelve la variable http_response
    return http_response

def formulario_consumibles(request):
        # Creamos contexto para trabajar con parámetros.
    context = {}

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= 'formulario-consumibles.html',
        context= context
    )
    # Devuelve la variable http_response
    return http_response

# Vistas de listas
def lista_heroes(request):
        # Creamos contexto para trabajar con parámetros.
    context = {}

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= 'lista-heroes.html',
        context= context
    )
    # Devuelve la variable http_response
    return http_response

def lista_armas(request):
        # Creamos contexto para trabajar con parámetros.
    context = {}

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= 'lista-armas.html',
        context= context
    )
    # Devuelve la variable http_response
    return http_response

def lista_consumibles(request):
        # Creamos contexto para trabajar con parámetros.
    context = {}

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= 'lista-consumibles.html',
        context= context
    )
    # Devuelve la variable http_response
    return http_response

