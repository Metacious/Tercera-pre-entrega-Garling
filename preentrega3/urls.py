from django.urls import path
from preentrega3.views import (dota, lista_heroes, lista_armas, lista_consumibles, 
                               crear_heroe, crear_arma, crear_consumible, 
                               buscar_heroe, buscar_arma, buscar_consumible)

urlpatterns = [
    path('', dota, name="index"),
    path('heroes', lista_heroes, name="heroes"),
    path('armas/', lista_armas, name="armas"),
    path('consumibles', lista_consumibles, name="consumibles"),
    path('crear-heroe/', crear_heroe, name="crear-heroe"),
    path('crear-arma/', crear_arma, name="crear-arma"),
    path('crear-consumible/', crear_consumible, name="crear-consumible"),
    path('buscar-heroe/', buscar_heroe, name='buscar-heroe'),
    path('buscar-arma/', buscar_arma, name='buscar-arma'),
    path('buscar-consumible/', buscar_consumible, name='buscar-consumible'),
]