# home_app/context_processors.py
from .models import Empresa

def custom_context(request):
    empresa_info = Empresa.objects.first()  # Ajusta esta lógica según tus necesidades
    return {
        'empresa_info': empresa_info,
    }