"""
URL configuration for wingwavestore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from src.views import home
from user.views import register, login, me, datos_envio, datos_pago
from django.contrib.auth.views import LogoutView
from product.views import catalogo  
from cart.views import carrito, addCarrito, sumCarrito, restCarrito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('user/register/', register, name='register'),
    path('user/login/', login, name='login'),
    path('user/logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('products/', catalogo, name='catalogo'),
    path('user/me/', me, name='me'),
    path('user/datos_envio/', datos_envio, name='datos_envio'),
    path('user/datos_pago/', datos_pago, name='datos_pago'),
    path('cart/', carrito, name='cart'),
    path('cart/add/<int:producto_id>/', addCarrito, name='addCarrito'),
    path('cart/sum/<int:producto_id>/', sumCarrito, name='sumCarrito'),
    path('cart/dec/<int:producto_id>/', restCarrito, name='restCarrito'),]
