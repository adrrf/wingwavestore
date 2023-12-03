from django.shortcuts import render
from .models import Producto
from django.db.models import Q


# Create your views here.
def catalogo(request):
    products = Producto.objects.all()
    choices_fabricante = Producto.fabricante.field.choices
    lista_fabricante = []
    for c in choices_fabricante:
        lista_fabricante.append(c[1])

    busqueda = request.GET.get('buscar')
    marca = request.GET.get('marca')
    if busqueda:
        products = Producto.objects.filter(
            Q(nombre__icontains=busqueda)
        ).distinct()
    elif marca:
        products = Producto.objects.filter(
            Q(fabricante__icontains=marca)
        ).distinct()
    
    context = {'products': products, 'choices_fabricante': lista_fabricante} 
    return render(request, 'product/catalogo.html', context)

def accesorios(request):
    products = Producto.objects.all()
    choices_fabricante = Producto.fabricante.field.choices
    lista_fabricante = []
    for c in choices_fabricante:
        lista_fabricante.append(c[1])

    busqueda = request.GET.get('buscar')
    marca = request.GET.get('marca')
    if busqueda:
        products = Producto.objects.filter(
            Q(nombre__icontains=busqueda)
        ).distinct()
    elif marca:
        products = Producto.objects.filter(
            Q(fabricante__icontains=marca)
        ).distinct()

    context = {'products': products, 'choices_fabricante': lista_fabricante}    
    return render(request, 'product/accesorios.html', context)

def drones(request):
    products = Producto.objects.all()
    choices_fabricante = Producto.fabricante.field.choices
    lista_fabricante = []
    for c in choices_fabricante:
        lista_fabricante.append(c[1])

    busqueda = request.GET.get('buscar')
    marca = request.GET.get('marca')
    if busqueda:
        products = Producto.objects.filter(
            Q(nombre__icontains=busqueda)
        ).distinct()
    elif marca:
        products = Producto.objects.filter(
            Q(fabricante__icontains=marca)
        ).distinct()

    context = {'products': products, 'choices_fabricante': lista_fabricante}
    return render(request, 'product/drones.html', context)

def piezas(request):
    products = Producto.objects.all()
    choices_fabricante = Producto.fabricante.field.choices
    lista_fabricante = []
    for c in choices_fabricante:
        lista_fabricante.append(c[1])

    busqueda = request.GET.get('buscar')
    marca = request.GET.get('marca')
    if busqueda:
        products = Producto.objects.filter(
            Q(nombre__icontains=busqueda)
        ).distinct()
    elif marca:
        products = Producto.objects.filter(
            Q(fabricante__icontains=marca)
        ).distinct()

    context = {'products': products, 'choices_fabricante': lista_fabricante}    
    return render(request, 'product/piezas.html', context)
        
def vista_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    choices_fabricante = Producto.fabricante.field.choices
    lista_fabricante = []
    for c in choices_fabricante:
        lista_fabricante.append(c[1])

    busqueda = request.GET.get('buscar')
    marca = request.GET.get('marca')
    if busqueda:
        products = Producto.objects.filter(
            Q(nombre__icontains=busqueda)
        ).distinct()
    elif marca:
        products = Producto.objects.filter(
            Q(fabricante__icontains=marca)
        ).distinct()
    
    context = {'producto': producto, 'choices_fabricante': lista_fabricante}
    return render(request, 'product/producto.html', context)