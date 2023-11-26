from django.shortcuts import render, redirect
from django.contrib import messages
import re
from order.models import Pedido
from cart.models import ProductoPedido
from product.models import Producto
from user.models import Cliente
from user.models import Datos_envio
# Create your views here.

def checkout(request):
    if request.method == 'GET':
        try:
            user = request.user
            cliente = Cliente.objects.get(user=user)
            device = request.COOKIES['device']
            cliente.device = device
            cliente.save()
        except:
            device = request.COOKIES['device']
            cliente = Cliente.objects.get(dispositivo=device)
        order = Pedido.objects.get(cliente=cliente, completado=False)
        if order.productopedido_set.all().count() == 0:
            return redirect('catalogo')
        items = order.productopedido_set.all()
        total = 0
        for item in items:
            total += item.producto.precio * item.cantidad
        order.total = total
        if total >= 50:
            envio = 0
            order.precio_envio = envio
        else:
            envio = 4.99
            order.precio_envio = envio
        order.save()
        context = {'items': items, 'order': order, 'total': total, 'envio': envio, 'total_envio': total + envio, 'cliente': cliente}

        return render(request, 'order/checkout.html', context)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        email = request.POST['email']
        calle = request.POST['calle']
        numero = request.POST['numero']
        puerta = request.POST['puerta']
        codigo_postal = request.POST['codigopostal']
        ciudad = request.POST['ciudad']
        provincia = request.POST['provincia']
        pais = request.POST['pais']
        pago = request.POST['pago']

        if nombre == '' or apellidos == '' or email == '' or calle == '' or numero == '' or codigo_postal == '' or ciudad == '' or provincia == '' or pais == '' or pago == '':
            messages.error(request, 'Por favor, rellene todos los campos')
        else:
            #validate mail regex
            email_valid = re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)
            if not email_valid:
                messages.error(request, 'El email no es válido')
            else:
                try:
                    user = request.user
                    cliente = Cliente.objects.get(user=user)
                    device = request.COOKIES['device']
                    cliente.device = device
                    cliente.save()
                except:
                    device = request.COOKIES['device']
                    cliente = Cliente.objects.get(dispositivo=device)
                order = Pedido.objects.get(cliente=cliente, completado=False)
                order.nombre = nombre
                order.apellido = apellidos
                order.email = email
                order.calle = calle
                order.numero = numero
                order.puerta = puerta
                order.codigo_postal = codigo_postal
                order.ciudad = ciudad
                order.provincia = provincia
                order.pais = pais
                order.metodo_pago = pago
                order.completado = True
                order.estado = 'PENDIENTE'
                order.save()
                items = order.productopedido_set.all()
                for item in items:
                    producto = Producto.objects.get(id=item.producto.id)
                    producto.stock -= item.cantidad
                    producto.save()
                messages.success(request, 'Pedido realizado correctamente')
                #redirect to pedidos detail
                return redirect('home')
        return render(request, 'order/checkout.html')