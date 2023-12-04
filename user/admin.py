from django.contrib import admin
from user.models import Datos_envio, Reclamacion, MensajeReclamacion

class Datos_envioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Datos_envio, Datos_envioAdmin)

class MensajeReclamacionInline(admin.TabularInline):
    model = MensajeReclamacion

class ReclamacionAdmin(admin.ModelAdmin):
    inlines = (MensajeReclamacionInline,)
    list_display = ('id', 'fecha', 'estado')
    list_filter = ('estado',)
    search_fields = ('id',)
    ordering = ('-fecha',)
    readonly_fields = ('fecha',)

admin.site.register(Reclamacion, ReclamacionAdmin)
