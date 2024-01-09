# persona urls.py
from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('cliente/new/', views.cliente_create, name='cliente_create'),
    path('cliente/<int:pk>/edit/', views.cliente_edit, name='cliente_edit'),
    path('cliente/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
]