#
from django.urls import path
from .views import *

app_name = "reserva_app"

urlpatterns = [
    path('reservas/', reserva_list, name='reserva_list'),
    path('reservas_json/', reservas_json, name='reservas_json'),
    path('reserva/new/', reserva_create, name='reserva_create'),
    path('reserva/<int:pk>/edit/', reserva_edit, name='reserva_edit'),
    path('reserva/<int:pk>/delete/', reserva_delete, name='reserva_delete')
]