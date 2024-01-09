# persona/forms.py
from django import forms
from .models import Cliente
from django.core.exceptions import ValidationError


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('__all__')  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        celular = cleaned_data.get('celular')

        # Para que no se controle a sí mismo
        cliente_id = self.instance.id if self.instance else None

        # Validar que no haya otros clientes con el mismo número de teléfono
        if Cliente.objects.filter(celular=celular).exclude(id=cliente_id).exists():
            raise ValidationError('Ya existe un cliente con este número de teléfono.')

        return cleaned_data
