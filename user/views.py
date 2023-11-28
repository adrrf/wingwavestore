from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
import re
from bs4 import BeautifulSoup
from .models import Datos_envio, Datos_pago
from .forms import CreateUserForm, DatosEnvioForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@csrf_protect
def register(request):
    if request.method == 'POST': 
        error = ""
        usuario = request.POST.get('username')
        nombre = request.POST.get('first_name')
        apellidos = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password_confirmation = request.POST.get('password2')
        if not usuario:
            error += "El campo usuario es obligatorio. "
        if not nombre:
            error += "El campo nombre es obligatorio. "
        if not apellidos:
            error += "El campo apellidos es obligatorio. "
        if not email:
            error += "El campo email es obligatorio. "
        if re.match(r"[^@]+@[^@]+\.[^@]+", email) == None:
            error += " El email no es válido. "
        if not password:
            error += "El campo contraseña es obligatorio. "
        if not password_confirmation:
            error += "El campo repetir contraseña es obligatorio. "
        if password != password_confirmation:
            error += "Las contraseñas no coinciden. "
        if usuario and nombre and apellidos and email and password and password_confirmation:
            user_form = CreateUserForm(request.POST)
            if user_form.is_valid():
                user_form.save()
                return redirect('login')
            else:
                soup = BeautifulSoup(str(user_form.errors), "html.parser")
                errors = soup.find_all("ul", class_="errorlist")
                errors.pop(0)
                for error_field in errors:
                    error_field = error_field.text
                    error += error_field 
                    error += " "
        if error:
            messages.error(request, error)
        
    return render(request, 'user/register.html')

@csrf_protect
def login(request):
    if request.method == 'POST':
        error = ""
        usuario = request.POST.get('username')
        password = request.POST.get('password')
        if not usuario:
            error += "El campo usuario es obligatorio. "
        if not password:
            error += "El campo contraseña es obligatorio. "
        if usuario and password:
            user = authenticate(request, username=usuario, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                error += "Usuario o contraseña incorrectos. "
        if error:
            messages.error(request, error)

    return render(request, 'user/login.html')

def logoutUser(request):
     if request.method=="POST":
        logout(request)
        return redirect('home')
     
@login_required(login_url='login')
def me(request):
    return render(request, 'user/me.html')

def mis_pedidos(request):
    return render(request, 'user/mis_pedidos.html')

def datos_envio(request):
    if request.method == 'GET':
        user = request.user
        datos_envio = Datos_envio.objects.filter(user=user)
        if datos_envio:
            datos_envio = datos_envio[0]
            return render(request, 'user/datos_envio.html', {'calle': datos_envio.calle, 'numero': datos_envio.numero, 'puerta': datos_envio.puerta, 'codigo_postal': datos_envio.codigo_postal, 'ciudad': datos_envio.ciudad, 'provincia': datos_envio.provincia, 'pais': datos_envio.pais})
        return render(request, 'user/datos_envio.html')   
    if request.method == 'POST': 
        error = ""
        user = request.user
        calle = request.POST.get('calle')
        numero = request.POST.get('numero')
        puerta = request.POST.get('puerta')
        codigo_postal = request.POST.get('codigo_postal')
        provincia = request.POST.get('provincia')
        pais = request.POST.get('pais')
        if not calle:
            error += "El campo calle es obligatorio. "
        if not numero:
            error += "El campo numero es obligatorio. "
        if not puerta:
            error += "El campo puerta es obligatorio. "
        if not codigo_postal:
            error += "El campo codigo_postal es obligatorio. "
        if not provincia:
            error += "El campo provincia es obligatorio. "
        if not pais:
            error += "El campo pais es obligatorio. "
        if calle and numero and puerta and codigo_postal and provincia and pais:
            datos_envio_form = DatosEnvioForm(request.POST)
            if datos_envio_form.is_valid():
                previos = Datos_envio.objects.filter(user=user)
                if previos:
                    previos.delete()
                datos_envio = datos_envio_form.save()
                datos_envio.user = user
                datos_envio.save()
                messages.success(request, 'Tus datos de envío se han actualizado')
                return redirect('datos_envio')
            else:
                soup = BeautifulSoup(str(datos_envio_form.errors), "html.parser")
                errors = soup.find_all("ul", class_="errorlist")
                errors.pop(0)
                for error_field in errors:
                    error_field = error_field.text
                    error += error_field 
                    error += " "
        if error:
            messages.error(request, error)
    return render(request, 'user/datos_envio.html')

def datos_pago(request):
    if request.method == 'GET':
        user = request.user
        datos_pago = Datos_pago.objects.filter(user=user)
        if datos_pago:
            datos_pago = datos_pago[0]
            return render(request, 'user/datos_pago.html', {'titular': datos_pago.titular, 'numero_tarjeta': datos_pago.numero_tarjeta, 'caducidad': datos_pago.caducidad, 'cs': datos_pago.cs})
        return render(request, 'user/datos_pago.html')
    if request.method == 'POST': 
        error = ""
        user = request.user
        titular = request.POST.get('titular')
        numero_tarjeta = request.POST.get('numero_tarjeta')
        caducidad = request.POST.get('caducidad')
        cs = request.POST.get('cs')
        if not titular:
            error += "El campo titular es obligatorio. "
        if not numero_tarjeta:
            error += "El campo numero de tarjeta es obligatorio. "
        if not caducidad:
            error += "El campo caducidad es obligatorio. "
        if not cs:
            error += "El campo codigo de seguridad es obligatorio. "
        if titular and numero_tarjeta and caducidad and cs:
            datos_pago_form = DatosPagoForm(request.POST)
            if datos_pago_form.is_valid():
                previos = Datos_pago.objects.filter(user=user)
                if previos:
                    previos.delete()
                datos_pago = datos_pago_form.save()
                datos_pago.user = user
                datos_pago.save()
                messages.success(request, 'Tus datos de pago se han actualizado')
                return redirect('datos_pago')
            else:
                soup = BeautifulSoup(str(datos_pago_form.errors), "html.parser")
                errors = soup.find_all("ul", class_="errorlist")
                errors.pop(0)
                for error_field in errors:
                    error_field = error_field.text
                    error += error_field 
                    error += " "
        if error:
            messages.error(request, error)
    return render(request, 'user/datos_pago.html')