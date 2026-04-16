from django.urls import path

from . import views

app_name = 'asistencia'

urlpatterns = [
    path('', views.registrar_asistencia, name='registrar'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
]
