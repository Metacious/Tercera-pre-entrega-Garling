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

# READ
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

# CREATE
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
        template_name ='preentrega3/crear-heroe.html',
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
        template_name ='preentrega3/crear-arma.html',
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
        template_name ='preentrega3/crear-consumible.html',
        context = {'formulario_consumible' : formulario_consumible}
        )
    return http_response

# SEARCH
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
    
# DELETE
# Vistas para eliminar datos.
def eliminar_heroe(request, nombre_de_heroe):
    # Declarar héroe por eliminar.
    heroe_por_eliminar = Heroe.objects.get(nombre = nombre_de_heroe)
    # Eliminar con la función delete.
    heroe_por_eliminar.delete()
    # Volver al menú.
    heroes = Heroe.objects.all() # Trae a todos los héroes.
    context = {"heroes": heroes}
    # Definir variable http_response.
    http_response = render(
        request=request,
        template_name='preentrega3/lista-heroes.html',
        context=context,
    )
    # Entregar resultado.
    return http_response

def eliminar_arma(request, nombre_de_arma):
    # Declarar héroe por eliminar.
    arma_por_eliminar = Heroe.objects.get(nombre = nombre_de_arma)
    # Eliminar con la función delete.
    arma_por_eliminar.delete()
    # Volver al menú.
    armas = Heroe.objects.all() # Trae a todos los héroes.
    context = {"armas": armas}
    # Definir variable http_response.
    http_response = render(
        request=request,
        template_name='preentrega3/lista-armas.html',
        context=context,
    )
    # Entregar resultado.
    return http_response

def eliminar_consumible(request, nombre_de_consumible):
    # Declarar héroe por eliminar.
    consumible_por_eliminar = Heroe.objects.get(nombre = nombre_de_consumible)
    # Eliminar con la función delete.
    consumible_por_eliminar.delete()
    # Volver al menú.
    consumibles = Heroe.objects.all() # Trae a todos los héroes.
    context = {"consumibles": consumibles}
    # Definir variable http_response.
    http_response = render(
        request=request,
        template_name='preentrega3/lista-consumibles.html',
        context=context,
    )
    # Entregar resultado.
    return http_response

# UPDATE
# Vistas para editar un elemento.

def editar_heroe(request, nombre_de_heroe):
    heroe_por_editar = Heroe.objects.get(nombre = nombre_de_heroe)
    # Si se recibe un formulario POST entonces se editan los datos.
    if(request.method == "POST"):
        # Se usa el mismo formulario que se creó para agregar datos.
        formulario_heroe = HeroeFormulario(request.POST)

        print(formulario_heroe)

        if(formulario_heroe.is_valid):
            informacion_heroe = formulario_heroe.cleaned_data

            heroe_por_editar.nombre = informacion_heroe["nombre"]
            heroe_por_editar.tipo = informacion_heroe["tipo"]
            heroe_por_editar.aporte = informacion_heroe["aporte"]
            heroe_por_editar.vida = informacion_heroe["vida"]
            heroe_por_editar.velocidad = informacion_heroe["velocidad"]

            heroe_por_editar.save()
            # Definir variable http_response.
            http_response = render(
            request=request,
            template_name='preentrega3/lista-heroes.html'
            )

            return http_response
    else:
        formulario_heroe = HeroeFormulario(initial={"nombre": heroe_por_editar.nombre, "tipo": heroe_por_editar.tipo,
                                                    "aporte": heroe_por_editar.aporte, "vida": heroe_por_editar.vida, "velocidad": heroe_por_editar.velocidad})
        # Definir variable http_response.
        
    return render(request, 'preentrega3/editar-heroe.html', {"formulario_heroe": formulario_heroe, "nombre_de_heroe": nombre_de_heroe})

########

def editar_arma(request, nombre_de_heroe):
    heroe_por_editar = Heroe.objects.get(nombre = nombre_de_heroe)
    # Si se recibe un formulario POST entonces se editan los datos.
    if(request.method == "POST"):
        # Se usa el mismo formulario que se creó para agregar datos.
        formulario_heroe = HeroeFormulario(request.POST)

        print(formulario_heroe)

        if(formulario_heroe.is_valid):
            informacion_heroe = formulario_heroe.cleaned_data

            heroe_por_editar.nombre = informacion_heroe["nombre"]
            heroe_por_editar.tipo = informacion_heroe["tipo"]
            heroe_por_editar.aporte = informacion_heroe["aporte"]
            heroe_por_editar.vida = informacion_heroe["vida"]
            heroe_por_editar.velocidad = informacion_heroe["velocidad"]

            heroe_por_editar.save()
            # Definir variable http_response.
            http_response = render(
            request=request,
            template_name='preentrega3/lista-heroes.html'
            )

            return http_response
    else:
        formulario_heroe = HeroeFormulario(initial={"nombre": heroe_por_editar.nombre, "tipo": heroe_por_editar.tipo,
                                                    "aporte": heroe_por_editar.aporte, "vida": heroe_por_editar.vida, "velocidad": heroe_por_editar.velocidad})
        # Definir variable http_response.
        http_response = render(
        request=request,
        template_name='preentrega3/editar-heroe.html',
        formulario = {"formulario_heroe": formulario_heroe, "nombre_de_heroe": nombre_de_heroe}
            )
    return http_response

######

def editar_consumible(request, nombre_de_heroe):
    heroe_por_editar = Heroe.objects.get(nombre = nombre_de_heroe)
    # Si se recibe un formulario POST entonces se editan los datos.
    if(request.method == "POST"):
        # Se usa el mismo formulario que se creó para agregar datos.
        formulario_heroe = HeroeFormulario(request.POST)

        print(formulario_heroe)

        if(formulario_heroe.is_valid):
            informacion_heroe = formulario_heroe.cleaned_data

            heroe_por_editar.nombre = informacion_heroe["nombre"]
            heroe_por_editar.tipo = informacion_heroe["tipo"]
            heroe_por_editar.aporte = informacion_heroe["aporte"]
            heroe_por_editar.vida = informacion_heroe["vida"]
            heroe_por_editar.velocidad = informacion_heroe["velocidad"]

            heroe_por_editar.save()
            # Definir variable http_response.
            http_response = render(
            request=request,
            template_name='preentrega3/lista-heroes.html'
            )

            return http_response
    else:
        formulario_heroe = HeroeFormulario(initial={"nombre": heroe_por_editar.nombre, "tipo": heroe_por_editar.tipo,
                                                    "aporte": heroe_por_editar.aporte, "vida": heroe_por_editar.vida, "velocidad": heroe_por_editar.velocidad})
        # Definir variable http_response.
        http_response = render(
        request=request,
        template_name='preentrega3/editar-heroe.html',
        formulario = {"formulario_heroe": formulario_heroe, "nombre_de_heroe": nombre_de_heroe}
            )
    return http_response
