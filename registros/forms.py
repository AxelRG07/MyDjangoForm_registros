from django import forms
from .models import *
from django.core.validators import FileExtensionValidator

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'division', 'logo']

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'division': forms.TextInput(attrs={'class':'form-control'}),
        }

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'foto', 'identifacion_pdf']

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }