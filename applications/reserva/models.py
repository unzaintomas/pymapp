from django.db import models
from django.contrib.auth.models import User
from applications.persona.models import Cliente

# Create your models here.
class Reserva(models.Model):
    fecha_inicio = models.DateTimeField('Fecha y Hora de Inicio')
    fecha_fin = models.DateTimeField('Fecha y Hora de Fin')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    precio = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    operador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # Información de pagos
    senado = models.BooleanField('Seña pagada', default=False)
    pagado = models.BooleanField('Pagado totalmente', default=False)

    # Campo para rastrear si la reserva ha sido cancelada
    cancelada = models.BooleanField('Cancelar Reserva', default=False)

    def __str__(self):
        return f'Reserva para {self.cliente} - Operador: {self.operador.username if self.operador else "N/A"}'
    