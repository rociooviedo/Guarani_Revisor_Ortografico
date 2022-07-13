from django import forms
from django.forms.fields import CharField
from .models import Revisor

class FormularioPrincipal(forms.Form):
    texto = forms.CharField(max_length=1000)
    texto=forms.CharField(widget=forms.Textarea(attrs={'rows': 7, 'cols': 150}))
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
