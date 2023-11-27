from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.shortcuts import redirect, render

from .models import Heroe, Arma, Consumible, Avatar
from .forms import HeroeFormulario, ArmaFormulario, ConsumibleFormulario, AvatarFormulario

# Importar librerías de autenticación.
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Mixin y decoradores
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Perfil de usuario
from django.views.generic import UpdateView
from .forms import UserRegisterForm, UserUpdateForm

# Mensajes
from django.contrib import messages


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

# Página about us.
def about(request):
    # Creamos contexto para trabajar con parámetros.
    context = {}

    # Asignamos render para mostrar el archivo html.
    http_response = render(
        request = request,
        template_name= 'preentrega3/about.html',
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
@login_required
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

            heroe = Heroe(nombre = nombre, tipo = tipo, aporte = aporte, vida = vida, velocidad = velocidad, creador = request.user)           
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

@login_required
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
                creador = request.user
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

@login_required
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
                creador = request.user
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
@login_required
def eliminar_heroe(request, id_heroe):
    # Declarar héroe por eliminar.
    heroe_por_eliminar = Heroe.objects.filter(id = id_heroe)
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

@login_required
def eliminar_arma(request, id_de_arma):
    # Declarar héroe por eliminar.
    arma_por_eliminar = Arma.objects.get(id = id_de_arma)
    # Eliminar con la función delete.
    arma_por_eliminar.delete()
    # Volver al menú.
    armas = Arma.objects.all() # Trae a todos los héroes.
    context = {"armas": armas}
    # Definir variable http_response.
    http_response = render(
        request=request,
        template_name='preentrega3/lista-armas.html',
        context=context,
    )
    # Entregar resultado.
    return http_response

@login_required
def eliminar_consumible(request, id_de_consumible):
    # Declarar héroe por eliminar.
    consumible_por_eliminar = Consumible.objects.get(id = id_de_consumible)
    # Eliminar con la función delete.
    consumible_por_eliminar.delete()
    # Volver al menú.
    consumibles = Consumible.objects.all() # Trae a todos los héroes.
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

@login_required
def editar_heroe(request, id_de_heroe):
    heroe_por_editar = Heroe.objects.get(id = id_de_heroe)
    # Si se recibe un formulario POST entonces se editan los datos.
    if(request.method == "POST"):
        # Se usa el mismo formulario que se creó para agregar datos.
        formulario_heroe = HeroeFormulario(request.POST)

        print(formulario_heroe)

        if(formulario_heroe.is_valid()):
            informacion_heroe = formulario_heroe.cleaned_data

            heroe_por_editar.nombre = informacion_heroe["nombre"]
            heroe_por_editar.tipo = informacion_heroe["tipo"]
            heroe_por_editar.aporte = informacion_heroe["aporte"]
            heroe_por_editar.vida = informacion_heroe["vida"]
            heroe_por_editar.velocidad = informacion_heroe["velocidad"]

            heroe_por_editar.save()
            # Definir variable http_response.
            #http_response = render(
            #request=request,
            #template_name='preentrega3/lista-heroes.html')

            return render(request, 'preentrega3/lista-heroes.html')
    else:
        formulario_heroe = HeroeFormulario(initial={"nombre": heroe_por_editar.nombre, "tipo": heroe_por_editar.tipo,
                                                    "aporte": heroe_por_editar.aporte, "vida": heroe_por_editar.vida, "velocidad": heroe_por_editar.velocidad})
        # Definir variable http_response.
        
    return render(request, 'preentrega3/editar-heroe.html', {"formulario_heroe": formulario_heroe, "id_de_heroe": id_de_heroe})

########

@login_required
def editar_arma(request, id_de_arma):
    arma_por_editar = Arma.objects.get(id = id_de_arma)
    # Si se recibe un formulario POST entonces se editan los datos.
    if(request.method == "POST"):
        # Se usa el mismo formulario que se creó para agregar datos.
        formulario_arma = ArmaFormulario(request.POST)

        print(formulario_arma)

        if(formulario_arma.is_valid):
            informacion_arma = formulario_arma.cleaned_data

            arma_por_editar.nombre = informacion_arma['nombre']
            arma_por_editar.rareza = informacion_arma['rareza']
            arma_por_editar.descripcion = informacion_arma['descripcion']
            arma_por_editar.costo = informacion_arma['costo']

            arma_por_editar.save()
            # Definir variable http_response.
            http_response = render(
            request=request,
            template_name='preentrega3/lista-armas.html'
            )

            return http_response
    else:
        formulario_arma = ArmaFormulario(initial={"nombre": arma_por_editar.nombre, "rareza": arma_por_editar.rareza,
                                                    "descripcion": arma_por_editar.descripcion, "costo": arma_por_editar.costo})
        
    return render(request, 'preentrega3/editar-arma.html', {"formulario_arma": formulario_arma, "id_de_arma": id_de_arma})


######

@login_required
def editar_consumible(request, id_de_consumible):
    consumible_por_editar = Consumible.objects.get(id = id_de_consumible)
    # Si se recibe un formulario POST entonces se editan los datos.
    if(request.method == "POST"):
        # Se usa el mismo formulario que se creó para agregar datos.
        formulario_consumible = ConsumibleFormulario(request.POST)

        print(formulario_consumible)

        if(formulario_consumible.is_valid()):
            informacion_consumible = formulario_consumible.cleaned_data

            consumible_por_editar.nombre = informacion_consumible["nombre"]
            consumible_por_editar.rareza = informacion_consumible["rareza"]
            consumible_por_editar.descripcion = informacion_consumible["descripcion"]
            consumible_por_editar.sanacion = informacion_consumible["sanacion"]
            consumible_por_editar.duracion = informacion_consumible["duracion"]
            consumible_por_editar.costo = informacion_consumible["costo"]

            consumible_por_editar.save()

            return render(request, 'preentrega3/lista-consumibles.html')
    else:
        formulario_consumible = ConsumibleFormulario(initial={"nombre": consumible_por_editar.nombre, "rareza": consumible_por_editar.rareza,
                                                    "descripcion": consumible_por_editar.descripcion, "sanacion": consumible_por_editar.sanacion,
                                                    "duracion": consumible_por_editar.duracion, "costo": consumible_por_editar.costo})
    
    return render(request, 'preentrega3/editar-consumible.html', {"formulario_consumible": formulario_consumible, "id_de_consumible": id_de_consumible})

# SISTEMA LOGIN

# Vista para el ingreso de usuarios.
def login_request(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = clave)

            if user:
                login(request = request, user = user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('index')
                return redirect(url_exitosa)
            else:
                return render(request, "preentrega3/index.html", {"mensaje": "Error, datos incorrectos"})
        else:
            return render(request, "preentrega3/index.html", {"mensaje": "Error, formulario inválido"})
    # Cuando no sea método POST.
    form = AuthenticationForm()
    return render(request, "preentrega3/login.html", {"form" : form})

# Registro
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "preentrega3/registro.html", {"mensaje": "Usuario creado"})
    else:
        form = UserCreationForm()
    
    return render(request, "preentrega3/registro.html", {"form": form})

# Actualizar perfil de usuario.
###class MiPerfilUpdateView(LoginRequiredMixin, UserUpdateForm):
   # form_class = UserUpdateForm
  #  success_url = reverse_lazy('index')
 #   template_name = 'preentrega3/formulario_perfil.html'
#
#   def get_object(self, queryset = None):
#        return self.request.user###

@login_required
def actualizar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance = usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha actualizado el perfil de usuario')
            url_exitosa = reverse('index')
            return redirect(url_exitosa)
    else:
        form = UserUpdateForm(instance = usuario)
    return render(request, 'preentrega3/formulario_perfil.html', {'form': form})


    
# Edición de avatar
def agregar_avatar(request):
    if request.method == "POST":
        formulario_avatar = AvatarFormulario(request.POST, request.FILES)
        
        if formulario_avatar.is_valid():
            existing_avatar = Avatar.objects.filter(user=request.user).first()
            if existing_avatar:
                # Actualiza el avatar existente
                existing_avatar.imagen = formulario_avatar.cleaned_data['imagen']
                existing_avatar.save()
            else:
                # Crea un avatar nuevo para el usuario
                avatar = formulario_avatar.save(commit=False)
                avatar.user = request.user
                avatar.save()
    else:
        formulario_avatar = AvatarFormulario()
    return render(request = request,
                  template_name = 'preentrega3/formulario_avatar.html',
                  context = {'formulario_avatar': formulario_avatar})





    