from django.db import models
from django.core.validators import RegexValidator


class Solicitud(models.Model):
    TIPO_SOLICITUD_OPCIONES = [
        ("academica", "Academica"),
        ("administrativa", "Administrativa"),
        ("tecnica", "Tecnica"),
        ("otra", "Otra"),
    ]

    nombre_solicitante = models.CharField(max_length=150)
    documento_identidad = models.CharField(max_length=30)
    correo_electronico = models.EmailField(max_length=150)
    telefono_contacto = models.CharField(max_length=20,validators=[RegexValidator(r"^\d+$", "El telefono debe contener solo numeros.")],)
    tipo_solicitud = models.CharField(max_length=20, choices=TIPO_SOLICITUD_OPCIONES)
    asunto = models.CharField(max_length=150)
    descripcion_detallada = models.TextField()
    fecha_solicitud = models.DateField()
    archivo_adjunto = models.FileField(upload_to="solicitudes/", blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_solicitante} - {self.asunto}"
