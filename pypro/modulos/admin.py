from django.contrib import admin

from pypro.modulos.models import Modulo, Aula

admin.site.register([Modulo, Aula])
