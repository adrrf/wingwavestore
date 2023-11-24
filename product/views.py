from django.shortcuts import render
from .models import Producto

# Create your views here.
def catalogo(request):
    products = Producto.objects.all()
    context = {'products': products}
    return render(request, 'product/catalogo.html', context)

