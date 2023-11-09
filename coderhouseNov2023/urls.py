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
from preentrega3.views import dota, formulario_heroes, formulario_armas, formulario_consumibles, lista_heroes, lista_armas, lista_consumibles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dota', dota),
    path('formulario-heroes', formulario_heroes),
    path('formulario-armas', formulario_armas),
    path('formulario-consumibles', formulario_consumibles),
    path('lista-heroes', lista_heroes),
    path('lista-armas', lista_armas),
    path('lista-consumibles', lista_consumibles),
]
