# Generated by Django 5.0 on 2024-01-08 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0005_remove_reserva_hora_fin_remove_reserva_hora_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cancelada',
            field=models.BooleanField(default=False, verbose_name='Cancelar Reserva'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_fin',
            field=models.DateTimeField(verbose_name='Fecha y Hora de Fin'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_inicio',
            field=models.DateTimeField(verbose_name='Fecha y Hora de Inicio'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='pagado',
            field=models.BooleanField(default=False, verbose_name='Pagado totalmente'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='senado',
            field=models.BooleanField(default=False, verbose_name='Seña pagada'),
        ),
    ]