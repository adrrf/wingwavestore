from django.shortcuts import render
from .models import Producto
from django.db.models import Q


# Create your views here.
def catalogo(request):
    products = Producto.objects.all()
    choices_fabricante = Producto.fabricante.field.choices
    choices_seccion = Producto.seccion.field.choices
    lista_fabricante = []
    lista_seccion = []
    for c in choices_fabricante:
        lista_fabricante.append(c[1])

    for c in choices_seccion:
        lista_seccion.append(c[1])

    busqueda = request.GET.get('buscar')
    marca = request.GET.get('marca')
    seccion = request.GET.get('seccion')
    if busqueda:
        products= products.filter(
            Q(nombre__icontains=busqueda)
        ).distinct()
    if marca:
        products = products.filter(
            Q(fabricante__icontains=marca)
        ).distinct()
    if seccion:
        products = products.filter(
            Q(seccion__icontains=seccion)
        ).distinct()
    
    context = {'products': products, 'choices_fabricante': lista_fabricante, 'choices_seccion': lista_seccion} 
    return render(request, 'product/catalogo.html', context)

def accesorios(request):
    products = Producto.objects.all()
    choices_fabricante = Producto.fabricante.field.choices
    choices_seccion = Producto.seccion.field.choices
    lista_fabricante = []
    lista_seccion = []
    for c in choices_fabricante:
        lista_fabricante.append(c[1])

    for c in choices_seccion:
        lista_seccion.append(c[1])

    busqueda = request.GET.get('buscar')
    marca = request.GET.get('marca')
    seccion = request.GET.get('seccion')
    if busqueda:
        products= products.filter(
            Q(nombre__icontains=busqueda)
        ).distinct()
    if marca:
        products = products.filter(
            Q(fabricante__icontains=marca)
        ).distinct()
    if seccion:
        products = products.filter(
            Q(seccion__icontains=seccion)
        ).distinct()
    
    context = {'products': products, 'choices_fabricante': lista_fabricante, 'choices_seccion': lista_seccion}     
    return render(request, 'product/accesorios.html', context)

def drones(request):
    products = Producto.objects.all()
    choices_fabricante = Producto.fabricante.field.choices
    choices_seccion = Producto.seccion.field.choices
    lista_fabricante = []
    lista_seccion = []
    for c in choices_fabricante:
        lista_fabricante.append(c[1])

    for c in choices_seccion:
        lista_seccion.append(c[1])

    busqueda = request.GET.get('buscar')
    marca = request.GET.get('marca')
    seccion = request.GET.get('seccion')
    if busqueda:
        products= products.filter(
            Q(nombre__icontains=busqueda)
        ).distinct()
    if marca:
        products = products.filter(
            Q(fabricante__icontains=marca)
        ).distinct()
    if seccion:
        products = products.filter(
            Q(seccion__icontains=seccion)
        ).distinct()
    
    context = {'products': products, 'choices_fabricante': lista_fabricante, 'choices_seccion': lista_seccion} 
    return render(request, 'product/drones.html', context)

def piezas(request):
    products = Producto.objects.all()
    choices_fabricante = Producto.fabricante.field.choices
    choices_seccion = Producto.seccion.field.choices
    lista_fabricante = []
    lista_seccion = []
    for c in choices_fabricante:
        lista_fabricante.append(c[1])

    for c in choices_seccion:
        lista_seccion.append(c[1])

    busqueda = request.GET.get('buscar')
    marca = request.GET.get('marca')
    seccion = request.GET.get('seccion')
    if busqueda:
        products= products.filter(
            Q(nombre__icontains=busqueda)
        ).distinct()
    if marca:
        products = products.filter(
            Q(fabricante__icontains=marca)
        ).distinct()
    if seccion:
        products = products.filter(
            Q(seccion__icontains=seccion)
        ).distinct()
    
    context = {'products': products, 'choices_fabricante': lista_fabricante, 'choices_seccion': lista_seccion} 
    return render(request, 'product/piezas.html', context)
        
def vista_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    products = Producto.objects.all()
    choices_fabricante = Producto.fabricante.field.choices
    choices_seccion = Producto.seccion.field.choices
    lista_fabricante = []
    lista_seccion = []
    for c in choices_fabricante:
        lista_fabricante.append(c[1])

    for c in choices_seccion:
        lista_seccion.append(c[1])

    busqueda = request.GET.get('buscar')
    marca = request.GET.get('marca')
    seccion = request.GET.get('seccion')
    if busqueda:
        products = products.filter(
            Q(nombre__icontains=busqueda)
        ).distinct()
    if marca:
        products = products.filter(
            Q(fabricante__icontains=marca)
        ).distinct()
    if seccion:
        products = products.filter(
            Q(seccion__icontains=seccion)
        ).distinct()
    
    context = {'producto': producto, 'choices_fabricante': lista_fabricante, 'choices_seccion': lista_seccion, 'products': products}
    return render(request, 'product/producto.html', context)