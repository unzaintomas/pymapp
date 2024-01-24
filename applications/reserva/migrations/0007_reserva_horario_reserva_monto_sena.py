# Generated by Django 5.0 on 2024-01-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0006_alter_reserva_cancelada_alter_reserva_fecha_fin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='horario',
            field=models.CharField(choices=[('09-19', '09:00 - 19:00'), ('21-07', '21:00 - 07:00'), ('personalizado', 'Personalizado')], default='09-19', max_length=15, verbose_name='Horario'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='monto_sena',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Monto de Seña'),
        ),
    ]
