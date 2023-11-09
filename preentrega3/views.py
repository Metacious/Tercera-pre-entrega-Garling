from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

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

# Vistas para crear héroes, armas o consumibles.
def crear_heroe(request):
    if request.method == "POST":
        data = request.POST
        heroe = Heroe(
            #nombre = data[nombre],
            #tipo = data[tipo],
            #aporte = data[aporte],
            #vida = data[vida],
            #velocidad = data[velocidad]
            )
        heroe.save()
        exito = reverse("lista-heroes")
    else:
        return render(
            request=request,
            template_name="crear-heroe.html"
        )

def crear_arma(request):
    if request.method == "POST":
        data = request.POST
        arma = Arma(
            #nombre = data[nombre],
            #tipo = data[tipo],
            #aporte = data[aporte],
            #vida = data[vida],
            #velocidad = data[velocidad]
            )
        arma.save()
        exito = reverse("lista-armas")
    else:
        return render(
            request=request,
            template_name="crear-arma.html"
        )

def crear_consumible(request):
    if request.method == "POST":
        data = request.POST
        consumible = Consumible(
            #nombre = data[nombre],
            #tipo = data[tipo],
            #aporte = data[aporte],
            #vida = data[vida],
            #velocidad = data[velocidad]
            )
        consumible.save()
        exito = reverse("lista-consumibles")
    else:
        return render(
            request=request,
            template_name="crear-consumible.html"
        )

# Vistas para buscar héroes, armas o consumibles.
def buscar_heroe(request):
    pass

def buscar_arma(request):
    pass

def buscar_consumible(request):
    pass



