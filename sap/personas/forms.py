from django import forms
from django.forms import EmailInput, ModelForm

from personas.models import Persona, Domicilio


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets ={
            'email':EmailInput(attrs={'type':'email'})
        }

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
