from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField('Nombre de la Empresa', max_length=255)
    direccion = models.CharField('Direccion de la Empresa', max_length=50)

    def __str__(self):
        return self.nombre