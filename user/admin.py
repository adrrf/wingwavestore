from django.contrib import admin
from user.models import Datos_envio

class Datos_envioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Datos_envio, Datos_envioAdmin)
