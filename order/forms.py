from django import forms
from .models import Pedido

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'apellido', 'email', 'calle', 'numero', 'puerta', 'codigo_postal', 'ciudad', 'provincia', 'pais', 'tienda', 'metodo_pago']
        labels= {
            'nombre': 'Nombre',
            'apellido': 'Apellidos',
            'email': 'Email',
            'calle': 'Calle',
            'numero': 'Número',
            'puerta': 'Puerta (Si no tiene, poner 0)',
            'codigo_postal': 'Codigo postal',
            'ciudad': 'Ciudad',
            'provincia': 'Provincia',
            'pais': 'País',
            'metodo_pago': 'Método de pago',
            'tienda': 'Recoger en tienda',
            }
        