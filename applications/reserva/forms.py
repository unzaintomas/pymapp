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
                if field_name == 'fecha_inicio' or field_name == 'fecha_fin':
                    # Verificar si el widget tiene el atributo 'data-target'
                    if 'data-target' in field.widget.attrs:
                        field.widget.attrs['data-target'] += '#reservacioninicio'
                    else:
                        # Si no existe, establecerlo
                        field.widget.attrs['data-target'] = '#reservacioninicio'
                    

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        # Para que no se controle a sí misma
        reserva_id = self.instance.id if self.instance else None

        # Validar que la fecha y hora de fin no sean menores a la fecha y hora de inicio
        if fecha_fin and fecha_inicio and fecha_fin < fecha_inicio:
            raise ValidationError('La fecha y hora de fin no pueden ser menores a la fecha y hora de inicio.')

        # Validar que no haya otras reservas activas en el mismo rango de fechas
        if Reserva.objects.filter(fecha_inicio__lt=fecha_fin, fecha_fin__gt=fecha_inicio, cancelada=False).exclude(id=reserva_id).exists():
            raise ValidationError('Ya existe una reserva activa en ese rango de fechas y horarios.')

        return cleaned_data