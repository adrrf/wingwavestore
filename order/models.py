from django.db import models
from user.models import Cliente
# Create your models here.

class Pedido(models.Model):
    class MetodoPago(models.TextChoices):
        TARJETA = 'TARJETA'
        CONTRA_REEMBOLSO = 'CONTRA_REEMBOLSO'
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False, null=True, blank=False)
    calle = models.CharField(max_length=200, null=True)
    ciudad = models.CharField(max_length=200, null=True)
    numero = models.CharField(max_length=200, null=True)
    puerta = models.CharField(max_length=200, null=True)
    provincia = models.CharField(max_length=200, null=True)
    pais = models.CharField(max_length=200, null=True)
    codigo_postal = models.CharField(max_length=200, null=True)
    metodo_pago = models.CharField(max_length=200, null=True, choices=MetodoPago.choices)
    precio_envio = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    def __str__(self):
        return str(self.id)

    