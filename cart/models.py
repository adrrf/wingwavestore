from django.db import models

# Create your models here.

class ProductoPedido(models.Model):
    producto = models.ForeignKey('product.Producto', on_delete=models.CASCADE)
    pedido = models.ForeignKey('order.Pedido', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def total(self):
        total = self.producto.precio * self.cantidad
        return total