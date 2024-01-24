from django.db import models
from django.contrib.auth.models import User
from applications.persona.models import Cliente

# Create your models here.
class Reserva(models.Model):
    HORARIO_CHOICES = [
        ('09-19', '09:00 - 19:00'),
        ('21-07', '21:00 - 07:00'),
        ('personalizado', 'Personalizado'),
    ]

    horario = models.CharField('Horario', max_length=15, choices=HORARIO_CHOICES, default='09-19')
    fecha_inicio = models.DateField('Fecha de Inicio', auto_now=False, auto_now_add=False, null=False, blank=False)
    fecha_fin = models.DateField('Fecha de Fin', auto_now=False, auto_now_add=False, null=False, blank=False)
    hora_inicio = models.TimeField('Hora de fin', auto_now=False, auto_now_add=False, null=False, blank=False)
    hora_fin = models.TimeField('Hora de inicio', auto_now=False, auto_now_add=False, null=False, blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, blank=False)
    precio = models.DecimalField('Precio', max_digits=10, decimal_places=2, null=False, blank=False)
    operador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # Información de pagos
    senado = models.BooleanField('Seña pagada', default=False)
    monto_sena = models.DecimalField('Monto de Seña', max_digits=10, decimal_places=2, null=True, blank=True)
    pagado = models.BooleanField('Pagado totalmente', default=False)

    # Campo para rastrear si la reserva ha sido cancelada
    cancelada = models.BooleanField('Cancelar Reserva', default=False)

    def __str__(self):
        return f'Reserva para {self.cliente} - Operador: {self.operador.username if self.operador else "N/A"}'
    