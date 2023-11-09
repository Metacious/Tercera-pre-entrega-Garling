from django.shortcuts import render

from django.http import HttpResponse

# Página de inicio
def dota(request):
    return HttpResponse("Aquí está la lista de campeones de DotA")

# Vistas de formularios
def formulario_heroes(request):
    return HttpResponse("Aquí se coloca template")

def formulario_armas(request):
    return HttpResponse("Las armas del juego")

def formulario_consumibles(request):
    return HttpResponse("Los objetos que se consumen en el juego")

# Vistas de listas
def lista_heroes(request):
    return HttpResponse("Aquí se coloca template")

def lista_armas(request):
    return HttpResponse("Las armas del juego")

def lista_consumibles(request):
    return HttpResponse("Los objetos que se consumen en el juego")

