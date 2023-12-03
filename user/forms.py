from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Datos_envio, Datos_pago, Reclamacion, MensajeReclamacion
from order.models import Pedido

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", 'email', 'password1', 'password2']

class DatosEnvioForm(forms.ModelForm):
    class Meta:
        model = Datos_envio
        fields = ['calle', 'numero', 'puerta', 'codigo_postal', 'provincia', 'ciudad', 'pais']
        labels= {
            'calle': 'Calle',
            'numero': 'Número',
            'puerta': 'Puerta (Si no tiene, poner 0)',
            'codigo_postal': 'Codigo postal',
            'provincia': 'Provincia',
            'ciudad': 'Ciudad',
            'pais': 'País',
            }

class DatosPagoForm(forms.ModelForm):
    class Meta:
        model = Datos_pago
        fields = ['titular', 'numero_tarjeta', 'caducidad', 'cs']
        labels= {
            'titular': 'Titular',
            'numero_tarjeta': 'Número de tarjeta',
            'caducidad': 'caducidad',
            'cs': 'Codigo de seguridad',
            }

class ReclamacionForm(forms.Form):
    class Meta:
        model = Reclamacion
        fields = ['user', 'pedido_id', 'mensaje', 'estado']
        labels= {
            'user': 'Usuario',
            'pedido_id': 'Id del pedido',
            'mensaje': 'Mensaje',
            'estado': 'Estado'
        }

class MensajeReclamacionForm(forms.Form):
    class Meta:
        model = MensajeReclamacion
        fields =['reclamacion', 'user', 'mensaje']
        labels = {
            'reclamacion': 'Reclamacion',
            'user': 'Usuario',
            'mensaje': 'Mensaje'
        }