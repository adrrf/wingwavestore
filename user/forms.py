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
class ReclamacionForm(forms.ModelForm):
    class Meta:
        model = Reclamacion
        fields = ['user', 'mensaje']
        labels= {
            'user': 'User',
            'mensaje': 'Mensaje',
        }

class MensajeReclamacionForm(forms.ModelForm):
    class Meta:
        model = MensajeReclamacion
        fields =['mensaje']
        labels = {
            'mensaje': 'Mensaje'
        }
