from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    email = models.EmailField()
    contraseña = models.CharField(max_length=255)

class Datos_envio(models.Model):
    calle = models.CharField(max_length=255)
    numero = models.IntegerField()
    puerta = models.CharField(max_length=255)
    codigo_postal = models.IntegerField()
    provincia = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)

class Datos_pago(models.Model):
    titular = models.CharField(max_length=255)
    numero_tarjeta = models.CharField(max_length=255)
    caducidad = models.CharField(max_length=255)
    cs = models.IntegerField()