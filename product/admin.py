from django.contrib import admin
from .models import Producto, Opinion

# Register your models here.
class OpinionAdmin(admin.ModelAdmin):
    model = Opinion

admin.site.register(Producto)