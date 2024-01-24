from django.contrib import admin
from .models import Reserva


class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_inicio', 'fecha_fin', 'hora_inicio', 'hora_fin', 'precio', 'monto_sena', 'senado', 'pagado')

admin.site.register(Reserva, ReservaAdmin)