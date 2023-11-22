from django.db import models
from django import forms

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

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=255)
    calle = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    puerta = models.IntegerField()
    codigo_postal = models.IntegerField()
    provincia = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    metodo_pago = models.CharField(max_length=255)
    titular = models.CharField(max_length=255)
    numero_tarjeta = models.CharField(max_length=255)
    caducidad = models.CharField(max_length=255)
    cs = models.IntegerField()

class Datos_pago(models.Model):
    titular = models.CharField(max_length=255)
    numero_tarjeta = models.CharField(max_length=255)
    caducidad = models.CharField(max_length=255)
    cs = models.IntegerField()

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

class Pedido_producto(models.Model):
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Opinion(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=255)
    puntuacion = models.FloatField()

class Reclamacion(models.Model):
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Mensaje(models.Model):
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
