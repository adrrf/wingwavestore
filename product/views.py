from django.shortcuts import render, redirect
from .models import Producto, Opinion
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages


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
    opiniones = Opinion.objects.filter(producto= producto)
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
    
    context = {'producto': producto, 'choices_fabricante': lista_fabricante, 'choices_seccion': lista_seccion, 'products': products, 'opiniones': opiniones}
    return render(request, 'product/producto.html', context)

def add_opinion(request, producto_id):
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404("Reclamacion no encontrada")
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje')
        
        if mensaje:
            usuario = request.user if request.user.is_authenticated else None

            # Guardar la opinión en la base de datos
            opinion = Opinion.objects.create(
                mensaje=mensaje,
                producto_id=producto_id,
                usuario=usuario
            )
            
            messages.success(request, '¡Opinión añadida exitosamente!')
            return redirect(reverse('vistaProducto', args=[producto_id]))

    return render(request, 'product/add_opinion.html', {'producto': producto})