from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
import re
from bs4 import BeautifulSoup

# Create your views here.
from .forms import CreateUserForm

def home(request):
    return render(request, 'index.html')

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
                messages.success(request, "Usuario registrado correctamente")
            else:
                soup = BeautifulSoup(str(user_form.errors), "html.parser")
                errors = soup.find_all("ul", class_="errorlist")
                errors.pop(0)
                for error_field in errors:
                    print(error_field)
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
    return render(request, 'user/login.html')