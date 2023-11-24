from django.urls import path
# Recuerda agregar todas las vistas con import.
from preentrega3.views import (dota, lista_heroes, lista_armas, lista_consumibles, 
                               crear_heroe, crear_arma, crear_consumible, 
                               buscar_heroe, buscar_arma, buscar_consumible,
                               eliminar_heroe, eliminar_arma, eliminar_consumible,
                               editar_heroe, editar_arma, editar_consumible)

urlpatterns = [
    # Página de inicio.
    path('', dota, name="index"),
    # Mostrar elementos.
    path('heroes', lista_heroes, name="heroes"),
    path('armas/', lista_armas, name="armas"),
    path('consumibles', lista_consumibles, name="consumibles"),
    # Crear elementos.
    path('crear-heroe/', crear_heroe, name="crear-heroe"),
    path('crear-arma/', crear_arma, name="crear-arma"),
    path('crear-consumible/', crear_consumible, name="crear-consumible"),
    # Buscar elementos.
    path('buscar-heroe/', buscar_heroe, name='buscar-heroe'),
    path('buscar-arma/', buscar_arma, name='buscar-arma'),
    path('buscar-consumible/', buscar_consumible, name='buscar-consumible'),
    # Eliminar elementos.
    path('eliminar-heroe/<nombre_de_heroe>', eliminar_heroe, name='eliminar-heroe'),
    path('eliminar-arma/<nombre_de_arma>', eliminar_arma, name='eliminar-arma'),
    path('eliminar-consumible/<nombre_de_consumible>', eliminar_consumible, name='eliminar-consumible'),
    # Editar elementos.
    path('editar-heroe/<nombre_de_heroe>/', editar_heroe, name='editar-heroe'),
    path('editar-arma/<nombre_de_arma>/', editar_arma, name='editar-arma'),
    path('editar-consumible/<nombre_de_consumible>/', editar_consumible, name='editar-consumible'),
]