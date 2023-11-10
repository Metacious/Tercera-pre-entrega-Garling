from django.shortcuts import render

from django.http import HttpResponse
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import redirect

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
        formulario = HeroeFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            tipo = data["tipo"]
            aporte = data["aporte"]
            vida = data["vida"]
            velocidad = data["velocidad"]

            heroe = Heroe(nombre = nombre, tipo = tipo, aporte = aporte, vida = vida, velocidad = velocidad)           
            heroe.save()
            exito = reverse('lista-heroes')
            return redirect(exito)
    else: 
        formulario = HeroeFormulario()
    http_response = render(
        request = request,
        template_name ='preentrega3/lista-heroes.html',
        context = {'formulario' : formulario}
    )
    return http_response


def crear_arma(request):
    if request.method == 'POST':
        formulario = ArmaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
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
            exito = reverse('lista-armas')
            return redirect(exito)
    else: 
        formulario = ArmaFormulario()
    http_response = render(
        request = request,
        template_name ='preentrega3/lista-armas.html',
        context = {'formulario' : formulario}
        )
    return http_response

def crear_consumible(request):
    if request.method == 'POST':
        formulario = ConsumibleFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            rareza = data["rareza"]
            descripcion = data["descripcion"]
            sanacion = data["sanacion"]
            duracion = data["duracion"]
            costo = data["costo"]
            
            consumible = Arma(
                nombre = nombre,
                rareza = rareza,
                descripcion = descripcion,
                sanacion = sanacion,
                duracion = duracion,
                costo = costo,
                )           
            consumible.save()
            exito = reverse('lista-consumibles')
            return redirect(exito)
    else: 
        formulario = ConsumibleFormulario()
    http_response = render(
        request = request,
        template_name ='preentrega3/lista-consumibles.html',
        context = {'formulario' : formulario}
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
    
# Vistas de formularios
def formulario_heroe(request):
        # Creamos contexto para trabajar con parámetros.
    context = {
        'heroes' : Heroe.objects.all()
    }

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= 'preentrega3/formulario-heroe.html',
        context= context
    )
    # Devuelve la variable http_response
    return http_response

def formulario_arma(request):
        # Creamos contexto para trabajar con parámetros.
    context = {
        
    }

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= 'preentrega3/formulario-arma.html',
        context= context
    )
    # Devuelve la variable http_response
    return http_response

def formulario_consumible(request):
        # Creamos contexto para trabajar con parámetros.
    context = {
        
    }

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= 'preentrega3/formulario-consumible.html',
        context= context
    )
    # Devuelve la variable http_response
    return http_response




