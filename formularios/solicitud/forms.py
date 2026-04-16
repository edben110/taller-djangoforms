from django import forms

from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            "nombre_solicitante",
            "documento_identidad",
            "correo_electronico",
            "telefono_contacto",
            "tipo_solicitud",
            "asunto",
            "descripcion_detallada",
            "fecha_solicitud",
            "archivo_adjunto",
        ]
        widgets = {
            'nombre_solicitante': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su nombre completo',
            }),
            'documento_identidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su documento',
            }),
            'correo_electronico': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com',
            }),
            'telefono_contacto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de teléfono',
            }),
            'tipo_solicitud': forms.Select(attrs={
                'class': 'form-select',
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Asunto de la solicitud',
            }),
            'descripcion_detallada': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describa su solicitud en detalle',
            }),
            'fecha_solicitud': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'archivo_adjunto': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }
