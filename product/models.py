from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    seccion = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255)
    stock = models.IntegerField()