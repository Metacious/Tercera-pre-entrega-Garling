from django.urls import path, include
from preentrega3.views import dota, lista_heroes, lista_armas, lista_consumibles, crear_heroe, crear_arma, crear_consumible, buscar_heroe, buscar_arma, buscar_consumible


urlpatterns = [
    path('preentrega3/', dota, name="index"),
    path('preentrega3/', lista_heroes, name="heroes"),
    path('preentrega3/', lista_armas, name="armas"),
    path('preentrega3/', lista_consumibles, name="consumibles"),
    path('preentrega3/', crear_heroe, name="crear-heroe"),
    path('preentrega3/', crear_arma, name="crear-arma"),
    path('preentrega3/', crear_consumible, name="crear-consumible"),
    path('preentrega3/', buscar_heroe, name="buscar-heroe"),
    path('preentrega3/', buscar_arma, name="buscar-arma"),
    path('preentrega3/', buscar_consumible, name="buscar-consumible"),
]