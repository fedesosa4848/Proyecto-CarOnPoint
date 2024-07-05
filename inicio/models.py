from django.db import models

from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Vehiculo(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    combustible = models.CharField(max_length=20)
    ano_fabricacion = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='vehiculos/', null=True, blank=True)
    uploadDate = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

    def __str__(self):
        return f"Marca: {self.marca.title()}, Modelo: {self.modelo.title()}, Combustible: {self.combustible.title()}, Año de fabricación: {self.ano_fabricacion}"

    def clean(self):
        super().clean()
        ano_fabricacion_entero = int(self.ano_fabricacion)
        if ano_fabricacion_entero < 1980:
            raise ValidationError('El año de fabricación debe ser posterior a 1980.')

class Auto(Vehiculo):
    numero_puertas = models.PositiveIntegerField()

class Moto(Vehiculo):
    tipo_manillar = models.CharField(max_length=20)

class Camion(Vehiculo):
    capacidad_carga = models.PositiveIntegerField()

class Camioneta(Vehiculo):
    capacidad_pasajeros = models.PositiveIntegerField()
