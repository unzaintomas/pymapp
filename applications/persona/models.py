from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField('Nombre', max_length=60)
    celular = models.CharField('Nro. Celular', max_length=60)
    email = models.EmailField('Email', blank=True, null=True)

    def __str__(self):
        return self.nombre