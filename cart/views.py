from django.shortcuts import render, redirect
from order.models import Pedido
from cart.models import ProductoPedido
from product.models import Producto
from user.models import Cliente
from django.contrib import messages
# Create your views here.
def carrito(request):
    try:
        user = request.user
        cliente, created = Cliente.objects.get_or_create(user=user)
        device = request.COOKIES['device']
        cliente.device = device
        cliente.save()
    except:
        device = request.COOKIES['device']
        cliente, created = Cliente.objects.get_or_create(dispositivo=device)
    order, created = Pedido.objects.get_or_create(cliente=cliente, completado=False)
    if order.productopedido_set.all().count() == 0:
        messages.info(request, 'No hay productos en el carrito')
    items = order.productopedido_set.all()
    total = 0
    for item in items:
        total += item.producto.precio * item.cantidad
    if total >= 50:
        envio = 0
        order.precio_envio = envio
    else:
        envio = 4.99
        order.precio_envio = envio
    order.save()
    checkout = True
    for item in items:
        if item.producto.stock < item.cantidad:
            checkout = False
    context = {'items': items, 'order': order, 'total': total, 'envio': envio, 'total_envio': total + envio, 'checkout': checkout}
    return render(request, 'cart/carrito.html', context)

def addCarrito(request):
    if request.method == 'POST':
        producto_id = request.POST['producto_id']
        cantidad = request.POST['cantidad']
        if not cantidad:
            cantidad = 1
        else:
            cantidad = int(cantidad)
        producto = Producto.objects.get(id=producto_id)
        if producto.stock == 0:
            return redirect('cart')
        try:
            user = request.user
            cliente, created = Cliente.objects.get_or_create(user=user)
            device = request.COOKIES['device']
            cliente.device = device
            cliente.save()
        except:
            device = request.COOKIES['device']
            cliente, created = Cliente.objects.get_or_create(dispositivo=device)
        order, created = Pedido.objects.get_or_create(cliente=cliente, completado=False)
        orderItem, created = ProductoPedido.objects.get_or_create(producto=producto, pedido=order)
        if not orderItem.cantidad:
            orderItem.cantidad = cantidad
        else:
            if orderItem.cantidad + cantidad > producto.stock:
                messages.warning(request, 'No hay stock disponible')
                return redirect('cart')
            else:
                orderItem.cantidad = orderItem.cantidad + cantidad
        orderItem.save()
        return redirect('cart')

def sumCarrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if producto.stock == 0:
        messages.warning(request, 'No hay stock disponible')
        return redirect('cart')
    try:
        user = request.user
        cliente, created = Cliente.objects.get_or_create(user=user)
        device = request.COOKIES['device']
        cliente.device = device
        cliente.save()
    except:
        device = request.COOKIES['device']
        cliente, created = Cliente.objects.get_or_create(dispositivo=device)
    order, created = Pedido.objects.get_or_create(cliente=cliente, completado=False)
    orderItem, created = ProductoPedido.objects.get_or_create(producto=producto, pedido=order)
    if orderItem.cantidad == producto.stock:
        messages.warning(request, 'No hay stock disponible')
        return redirect('cart')
    orderItem.cantidad = orderItem.cantidad + 1
    orderItem.save()
    return redirect('cart')

def restCarrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if producto.stock == 0:
        messages.warning(request, 'No hay stock disponible')
        return redirect('cart')
    try:
        user = request.user
        cliente, created = Cliente.objects.get_or_create(user=user)
        device = request.COOKIES['device']
        cliente.device = device
        cliente.save()
    except:
        device = request.COOKIES['device']
        cliente, created = Cliente.objects.get_or_create(dispositivo=device)
    order, created = Pedido.objects.get_or_create(cliente=cliente, completado=False)
    orderItem, created = ProductoPedido.objects.get_or_create(producto=producto, pedido=order)
    if created:
        orderItem.delete()
        return redirect('cart')
    if orderItem.cantidad > 1:
        orderItem.cantidad = orderItem.cantidad - 1
        orderItem.save()
    else:
        if orderItem.cantidad == 1:
            orderItem.delete()
    return redirect('cart')
