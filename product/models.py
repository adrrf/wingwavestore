from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=255)
    departamento_choices= [
        ("Piezas", "Piezas"),
        ("Drones", "Drones"),
        ("Accesorios", "Accesorios"),
    ]
    departamento = models.CharField(max_length=255, choices= departamento_choices,)
    seccion_choices= [
        ("Electronico", "Electronico"),
        ("Analogico", "Analogico"),
        ("Carga", "Carga"),
        ("Vigilancia", "Vigilancia"),
        ("Fotografia", "Fotografia"),
        ("Videografia", "Videografia"),
        ("Cuadricoptero", "Cuadricoptero"),
        ("Hexacoptero", "Hexacoptero"),
        ("Agricola", "Agricola"),
        ("Recopilador", "Recopilador"),
        ("Envio", "Envio"),
    ]
    seccion = models.CharField(max_length=255, choices= seccion_choices,)
    fabricante_choices= [
        ("DJI", "DJI"),
        ("Parrot", "Parrot"),
        ("Yuneec", "Yuneec"),
        ("Autel", "Autel"),
        ("3DR", "3DR"),
        ("Skydio", "Skydio"),
        ("Walkera", "Walkera"),
        ("PowerVision", "PowerVision"),
        ("Hubsan", "Hubsan"),
    ]
    fabricante = models.CharField(max_length=255, choices= fabricante_choices,)
    stock = models.IntegerField()


class Opinion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='opiniones')
    mensaje = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)