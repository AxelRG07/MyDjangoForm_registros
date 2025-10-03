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
    identificacion_pdf = forms.FileField(
        label="Identificacion (PDF)",
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf'],
                message='Error: Solo se permiten archivos en formato PDF.'
            )
        ]
    )

    class Meta:
        model = Jugador
        fields = ['nombre', 'foto', 'identificacion_pdf']

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }