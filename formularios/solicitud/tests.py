from django.test import TestCase
from django.urls import reverse

from .models import Solicitud


class SolicitudViewsTests(TestCase):
	def test_formulario_crea_solicitud_y_redirige(self):
		response = self.client.post(
			reverse("solicitud:formulario"),
			{
				"nombre_solicitante": "Juan Perez",
				"documento_identidad": "ABC123456",
				"correo_electronico": "juan@example.com",
				"telefono_contacto": "3001234567",
				"tipo_solicitud": "academica",
				"asunto": "Consulta de notas",
				"descripcion_detallada": "Necesito revisar el historial academico.",
				"fecha_solicitud": "2026-04-16",
			},
		)

		self.assertRedirects(response, reverse("solicitud:confirmacion"))
		self.assertEqual(Solicitud.objects.count(), 1)

	def test_confirmacion_responde_ok(self):
		response = self.client.get(reverse("solicitud:confirmacion"))
		self.assertEqual(response.status_code, 200)
