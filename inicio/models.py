from django.db import models

from django.db import models
from django.core.exceptions import ValidationError

class Vehiculo(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    combustible = models.CharField(max_length=20)
    ano_fabricacion = models.PositiveIntegerField()

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Combustible: {self.combustible}, Año de fabricación: {self.ano_fabricacion}"

    def clean(self):
        super().clean()
        # Convierte ano_fabricacion a entero antes de la comparación
        ano_fabricacion_entero = int(self.ano_fabricacion)
        if ano_fabricacion_entero < 1980:
            raise ValidationError('El año de fabricación debe ser posterior a 1980.')


