
from .models import contacto
from django import forms
from django.forms import widgets



class IngresaInfo(forms.ModelForm):
    
    class Meta:
        model = contacto
        fields = '__all__' #agrega todos los datos

        widget = {
            "fecha_de_emicion": forms.SelectDateWidget()
        }
