from django.db import models

# Create your models here.
# Cada modelo representa una base de datos.
class Heroe(models.Model):
    nombre = models.CharField(max_length=32)
    tipo = models.CharField(max_length=16)
    aporte = models.CharField(max_length=16)
    vida = models.IntegerField(default=500) 
    velocidad = models.IntegerField(default=300)

    def __str__(self):
        return  f"{self.nombre}, {self.tipo}, {self.aporte}, {self.vida}, {self.velocidad}"


class Arma(models.Model):
    nombre = models.CharField(max_length=32)
    rareza = models.CharField(max_length=16)
    descripcion = models.CharField(max_length=256)
    costo = models.IntegerField(default=1000)

    def __str__(self):
        return f"{self.nombre}, {self.rareza}, {self.descripcion}, {self.costo}"

class Consumible(models.Model):
    nombre = models.CharField(max_length=32)
    rareza = models.CharField(max_length=16)
    descripcion = models.CharField(max_length=256)
    sanacion = models.IntegerField(default=0)
    duracion = models.IntegerField(default=5)
    costo = models.IntegerField(default=1000)

    def __str__(self):
        return f"{self.nombre}, {self.rareza}, {self.descripcion}, {self.sanacion}, {self.duracion}, {self.costo}"
