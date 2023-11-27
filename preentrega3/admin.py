from django.contrib import admin
from preentrega3.models import Heroe, Arma, Consumible
from .models import Avatar

# Register your models here.
admin.site.register(Heroe)
admin.site.register(Arma)
admin.site.register(Consumible)
admin.site.register(Avatar)

