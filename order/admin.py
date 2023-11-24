from django.contrib import admin
from .models import Pedido
from cart.models import ProductoPedido
# Register your models here.

class ProductoPedidoInline(admin.TabularInline):
    model = ProductoPedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = (ProductoPedidoInline,)
    list_display = ('id', 'cliente', 'completado', 'fecha')
    list_filter = ('completado',)
    search_fields = ('id',)
    ordering = ('-fecha',)
    readonly_fields = ('fecha',)
    fieldsets = (
        ('Datos del pedido', {
            'fields': ('cliente', 'fecha', 'completado')
        }),
        ('Datos de envío', {
            'fields': ('calle', 'numero', 'puerta', 'ciudad', 'provincia', 'pais', 'codigo_postal')
        }),
        ('Datos de pago', {
            'fields': ('metodo_pago',)
        }),
    )

admin.site.register(Pedido, PedidoAdmin)
