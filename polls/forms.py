from django import forms

from django.forms.fields import CharField
from django.forms.widgets import CheckboxSelectMultiple
from .models import Revisor


class FormularioPrincipal(forms.Form):
    texto = forms.CharField(max_length=500, min_length=5, widget=forms.TextInput(attrs={
        'class': 'form-control col-lg-6'
    }))
    class Meta:
        requiredMessage = 'Este campo es requerido'
        model = Revisor
        fields = ('texto')
        widgets = {
            'texto': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
        error_messages = {
        'texto': {
            'required': requiredMessage,
        }
        }
