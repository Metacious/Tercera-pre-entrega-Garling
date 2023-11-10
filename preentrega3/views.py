from django.shortcuts import render

from django.urls import reverse
from django.db.models import Q
from django.shortcuts import redirect, render

from .models import Heroe, Arma, Consumible
from .forms import HeroeFormulario, ArmaFormulario, ConsumibleFormulario

# Página de inicio
def dota(request):
    # Creamos contexto para trabajar con parámetros.
    context = {}

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= 'preentrega3/index.html',
        context= context                                                                                                                                                                                            
    )
    # Devuelve la variable http_response
    return http_response

# Vistas de listas
def lista_heroes(request):
        # Creamos contexto para trabajar con parámetros.
    context = {
        'heroes' : Heroe.objects.all()
    }

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= 'preentrega3/lista-heroes.html',
        context= context
    )
    # Devuelve la variable http_response
    return http_response

def lista_armas(request):
        # Creamos contexto para trabajar con parámetros.
    context = {
        'armas' : Arma.objects.all()
    }

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= 'preentrega3/lista-armas.html',
        context= context
    )
    # Devuelve la variable http_response
    return http_response

def lista_consumibles(request):
        # Creamos contexto para trabajar con parámetros.
    context = {
        'consumibles' : Consumible.objects.all()
    }

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= 'preentrega3/lista-consumibles.html',
        context= context
    )
    # Devuelve la variable http_response
    return http_response

# Vistas para crear héroes, armas o consumibles.
def crear_heroe(request):
    if request.method == "POST":
        formulario_heroe = HeroeFormulario(request.POST)

        if formulario_heroe.is_valid():
            data = formulario_heroe.cleaned_data
            nombre = data["nombre"]
            tipo = data["tipo"]
            aporte = data["aporte"]
            vida = data["vida"]
            velocidad = data["velocidad"]

            heroe = Heroe(nombre = nombre, tipo = tipo, aporte = aporte, vida = vida, velocidad = velocidad)           
            heroe.save()
            exito = reverse("heroes")
            return redirect(exito)
    else: 
        formulario_heroe = HeroeFormulario()
    http_response = render(
        request = request,
        template_name ='preentrega3/lista-heroes.html',
        context = {'formulario_heroe' : formulario_heroe}
    )
    return http_response


def crear_arma(request):
    if request.method == 'POST':
        formulario_arma = ArmaFormulario(request.POST)

        if formulario_arma.is_valid():
            data = formulario_arma.cleaned_data
            nombre = data["nombre"]
            rareza = data["rareza"]
            descripcion = data["descripcion"]
            costo = data["costo"]
            
            arma = Arma(
                nombre = nombre,
                rareza = rareza,
                descripcion = descripcion,
                costo = costo,
                )           
            arma.save()
            exito = reverse('armas')
            return redirect(exito)
    else: 
        formulario_arma = ArmaFormulario()
    http_response = render(
        request = request,
        template_name ='preentrega3/lista-armas.html',
        context = {'formulario_arma' : formulario_arma}
        )
    return http_response

def crear_consumible(request):
    if request.method == 'POST':
        formulario_consumible = ConsumibleFormulario(request.POST)

        if formulario_consumible.is_valid():
            data = formulario_consumible.cleaned_data
            nombre = data["nombre"]
            rareza = data["rareza"]
            descripcion = data["descripcion"]
            sanacion = data["sanacion"]
            duracion = data["duracion"]
            costo = data["costo"]
            
            consumible = Consumible(
                nombre = nombre,
                rareza = rareza,
                descripcion = descripcion,
                sanacion = sanacion,
                duracion = duracion,
                costo = costo,
                )           
            consumible.save()
            exito = reverse('consumibles')
            return redirect(exito)
    else: 
        formulario_consumible = ConsumibleFormulario()
    http_response = render(
        request = request,
        template_name ='preentrega3/lista-consumibles.html',
        context = {'formulario_consumible' : formulario_consumible}
        )
    return http_response


# Vistas para buscar héroes, armas o consumibles.
def buscar_heroe(request):
    if(request.method == "POST"):
        data = request.POST
        busqueda = data['busqueda']
        busqueda_heroes = Heroe.objects.filter(nombre__contains = busqueda)
        context = {'heroes' : busqueda_heroes,}
        http_response = render(
            request=request,
            template_name='preentrega3/lista-heroes.html',
            context=context,
        )
        return http_response
    
def buscar_arma(request):
    if(request.method == "POST"):
        data = request.POST
        busqueda = data['busqueda']
        busqueda_arma = Arma.objects.filter(nombre__contains = busqueda)
        context = {'armas' : busqueda_arma,}
        http_response = render(
            request=request,
            template_name='preentrega3/lista-armas.html',
            context=context,
        )
        return http_response
    
def buscar_consumible(request):
    if(request.method == "POST"):
        data = request.POST
        busqueda = data['busqueda']
        busqueda_consumible = Consumible.objects.filter(nombre__contains = busqueda)
        context = {'consumibles' : busqueda_consumible,}
        http_response = render(
            request=request,
            template_name='preentrega3/lista-consumibles.html',
            context=context,
        )
        return http_response