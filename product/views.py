from django.shortcuts import render
from .models import Producto

# Create your views here.
def catalogo(request):
    products = Producto.objects.all()
    context = {'products': products}
    return render(request, 'product/catalogo.html', context)
        
def vista_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    context = {'producto': producto}
    return render(request, 'product/producto.html', context)