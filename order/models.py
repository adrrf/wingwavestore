from django.db import models
from user.models import Cliente
# Create your models here.

class Pedido(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'PENDIENTE'
        ENVIADO = 'ENVIADO'
        ENTREGADO = 'ENTREGADO'
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False, null=True, blank=False)
    estado = models.CharField(max_length=200, null=True, choices=Estado.choices)
    nombre = models.CharField(max_length=200, null=True)
    apellido = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    tienda = models.BooleanField(null=True)
    calle = models.CharField(max_length=200, null=True)
    ciudad = models.CharField(max_length=200, null=True)
    numero = models.CharField(max_length=200, null=True)
    puerta = models.CharField(max_length=200, null=True)
    provincia = models.CharField(max_length=200, null=True)
    pais = models.CharField(max_length=200, null=True)
    codigo_postal = models.CharField(max_length=200, null=True)
    metodo_pago = models.BooleanField(default=False, null=True, blank=False)
    stripe_id = models.CharField(max_length=500, null=True)
    total = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    precio_envio = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    def __str__(self):
        return str(self.id)

    