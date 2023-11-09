"""
URL configuration for coderhouseNov2023 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from preentrega3.views import dota, lista_heroes, lista_armas, lista_consumibles, crear_heroe, crear_arma, crear_consumible, buscar_heroe, buscar_arma, buscar_consumible


urlpatterns = [
    path('preentrega3/', include("preentrega3.urls")),
    path('admin/', admin.site.urls),
    path("", dota, name="index"),
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
