# reservas/forms.py
from django import forms
from .models import Reserva
from django.core.exceptions import ValidationError

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['senado', 'cancelada', 'pagado']:
                field.widget.attrs['class'] = 'form-control'
                    

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        hora_inicio = cleaned_data.get('hora_inicio')
        hora_fin = cleaned_data.get('hora_fin')

        print(f"Fecha Inicio: {fecha_inicio}, Fecha Fin: {fecha_fin}")
        print(f"Hora Inicio: {hora_inicio}, Hora Fin: {hora_fin}")

        # Para que no se controle a sí misma
        reserva_id = self.instance.id if self.instance else None

        # Validar que la fecha y hora de fin no sean menores o iguales a la fecha y hora de inicio
        if fecha_fin and fecha_inicio and (fecha_fin < fecha_inicio or (fecha_fin == fecha_inicio and hora_fin <= hora_inicio)):
            raise ValidationError('La fecha y hora de fin no pueden ser menores o iguales a la fecha y hora de inicio.')

        # Validar que no haya otras reservas activas en el mismo rango de fechas y horas
        if Reserva.objects.filter(
            fecha_fin__gte=fecha_inicio,
            fecha_inicio__lte=fecha_fin,
            hora_fin__gte=hora_inicio,
            hora_inicio__lte=hora_fin,
            cancelada=False
        ).exclude(id=reserva_id).exists():
            raise ValidationError('Ya existe una reserva activa en ese rango de fechas y horarios.')

        return cleaned_data
