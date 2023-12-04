from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    dispositivo = models.CharField(max_length=255)

class Datos_envio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    calle = models.CharField(max_length=255)
    numero = models.IntegerField()
    puerta = models.CharField(max_length=255)
    codigo_postal = models.IntegerField()
    provincia = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)

class Datos_pago(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    tarjeta = models.BooleanField(null=True)
class Reclamacion(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    mensaje = models.CharField(max_length=2550)
    mensajes = models.TextField(blank=True, null = True)
    estado = models.BooleanField(default=False, null=True, blank=False)

class MensajeReclamacion(models.Model):
    reclamacion = models.ForeignKey(Reclamacion, on_delete= models.CASCADE)
    mensaje = models.CharField(max_length=2550)
    fecha = models.DateTimeField(auto_now_add=True)