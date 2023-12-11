from django.shortcuts import render, redirect
from django.contrib import messages
import re
from order.models import Pedido
from cart.models import ProductoPedido
from product.models import Producto
from user.models import Cliente
from user.models import Datos_envio
from django.core.mail import send_mail
import stripe
from django.conf import settings
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
        if items.count() == 0:
            return redirect('catalogo')
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
        try:
            tienda = request.POST['tienda']
            tienda = True
        except:
            tienda = False
        calle = request.POST['calle']
        numero = request.POST['numero']
        puerta = request.POST['puerta']
        codigo_postal = request.POST['codigopostal']
        ciudad = request.POST['ciudad']
        provincia = request.POST['provincia']
        pais = request.POST['pais']
        pago = bool(eval(request.POST['pago']))

        if (not tienda and (nombre == '' or apellidos == '' or email == '' or calle == '' or numero == '' or codigo_postal == '' or ciudad == '' or provincia == '' or pais == '' or pago == '')) or tienda and (nombre == '' or apellidos == '' or email == '' or pago == ''):
            messages.error(request, 'Por favor, rellene todos los campos')
        else:
            #validate mail regex
            email_valid = re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)
            # validate postal code regex
            postal_code_valid = re.search(r'^[0-9]{5}$', codigo_postal)
            # validate number regex
            number_valid = re.search(r'^[0-9]+$', numero)
            if not email_valid or (not tienda and not postal_code_valid) or (not tienda and not number_valid):
                messages.error(request, 'Datos no válidos')
                return redirect('checkout')
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
                order.tienda = tienda
                order.calle = calle
                order.numero = numero
                order.puerta = puerta
                order.codigo_postal = codigo_postal
                order.ciudad = ciudad
                order.provincia = provincia
                order.pais = pais
                order.metodo_pago = pago
                items = order.productopedido_set.all()
                for item in items:
                    producto = Producto.objects.get(id=item.producto.id)
                    producto.stock -= item.cantidad
                    producto.save()
                if order.metodo_pago:
                    stripe.api_key = settings.STRIPE_SECRET_KEY
                    domain = request.build_absolute_uri('/')[:-1]
                    checkout_session = stripe.checkout.Session.create(
                        payment_method_types=['card'],
                        line_items=[{
                            'price_data': {
                                'currency': 'eur',
                                'unit_amount': int((order.total + order.precio_envio) * 100),
                                'product_data': {
                                    'name': 'Compra en WingWave Store',
                                },
                            },
                            'quantity': 1,
                        }],
                        mode='payment',
                        success_url= domain + '/order/' + str(order.id),
                        cancel_url= domain + '/order/' + str(order.id) + '/cancel',
                        )
                    order.stripe_id = checkout_session.id
                    order.completado = True
                    order.estado = 'PENDIENTE'
                    order.save()
                    return redirect(checkout_session.url, code=303)
                else:
                    order.completado = True
                    order.estado = 'PENDIENTE'
                    order.save()
                texto = 'Hola ' + order.nombre + ' ' + order.apellido + ',\n\n' + 'Gracias por realizar tu pedido en WingWave Store.\n\n' + 'Tu pedido:\n\n'
                items = order.productopedido_set.all()
                for item in items:
                    texto += item.producto.nombre + ' x' + str(item.cantidad) + '\n'
                texto += '\nPrecio total: ' + str(order.total) + '€\n'
                texto += 'Precio envío: ' + str(order.precio_envio) + '€\n'
                texto += 'Precio total con envío: ' + str(order.total + order.precio_envio) + '€\n\n'
                texto += 'Datos de envío:\n\n'
                texto += 'Nombre: ' + order.nombre + ' ' + order.apellido + '\n'
                texto += 'Email: ' + order.email + '\n'
                if order.tienda:
                    texto += 'Recoger en tienda\n\n'
                else:
                    texto += 'Calle: ' + order.calle + '\n'
                    texto += 'Número: ' + order.numero + '\n'
                    texto += 'Puerta: ' + order.puerta + '\n'
                    texto += 'Código postal: ' + order.codigo_postal + '\n'
                    texto += 'Ciudad: ' + order.ciudad + '\n'
                    texto += 'Provincia: ' + order.provincia + '\n'
                    texto += 'País: ' + order.pais + '\n\n'
                texto += 'Método de pago: '
                if order.metodo_pago:
                    texto += 'Tarjeta de crédito\n\n'
                else:
                    texto += 'Contrareembolso\n\n'
                texto += 'Si tienes alguna duda, puedes contactar con nosotros en nuestra web'
                send_mail('WingWave Store - Pedido realizado', texto, 'wingwavestore@gmail.com', [order.email], fail_silently=False)
                return redirect('orderdetail', order.id)
        return redirect('checkout')

def details(request, order_id):
    order = Pedido.objects.get(completado=True, id=order_id)
    print(order.tienda)
    items = order.productopedido_set.all()
    total_envio = order.total + order.precio_envio
    context = {'items': items, 'order': order, 'total_envio': total_envio}
    return render(request, 'order/details.html', context)

def search(request):
    context = {'items': [], 'order': '', 'total_envio': ''}
    if request.method == 'POST':
        order_id = request.POST['order_id']
        try:
            order = Pedido.objects.get(id=order_id, completado=True)
            if not order.completado:
                messages.error(request, 'El pedido no ha sido completado')
            items = order.productopedido_set.all()
            total_envio = order.total + order.precio_envio
            context = {'items': items, 'order': order, 'total_envio': total_envio}
        except:
            messages.error(request, 'El pedido no existe')
    return render(request, 'order/search.html', context)
    
def cancel(request, order_id):
    order = Pedido.objects.get(id=order_id)
    order.nombre = ''
    order.apellido = ''
    order.email = ''
    order.calle = ''
    order.numero = ''
    order.puerta = ''
    order.codigo_postal = ''
    order.ciudad = ''
    order.provincia = ''
    order.pais = ''
    order.metodo_pago = ''
    order.total = 0
    order.precio_envio = 0
    order.stripe_id = ''
    order.completado = False
    order.estado = ''
    items = order.productopedido_set.all()
    for item in items:
        producto = Producto.objects.get(id=item.producto.id)
        producto.stock += item.cantidad
        producto.save()
    order.delete()
    messages.warning(request, 'Pedido cancelado')
    return redirect('cart')