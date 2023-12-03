from django.shortcuts import render
from product.models import Producto
from django.db.models import Q

def home(request):
    return render(request, 'index.html')

def busqueda(request):
    products = Producto.objects.all()
    busqueda = request.GET.get('buscar')
    if busqueda:
        products= products.filter(
            Q(nombre__icontains=busqueda)
        ).distinct()
    context = {'products': products}
    return render(request, 'product/catalogo.html', context)
