from django.db import models

from django.db import models
from django.core.exceptions import ValidationError

class Vehiculo(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    combustible = models.CharField(max_length=20)
    ano_fabricacion = models.PositiveIntegerField()

    def __str__(self):
        return f"Marca: {self.marca.title()}, Modelo: {self.modelo.title()}, Combustible: {self.combustible.title()}, Año de fabricación: {self.ano_fabricacion}"

    def clean(self):
        super().clean()
        # Convierte ano_fabricacion a entero antes de la comparación
        ano_fabricacion_entero = int(self.ano_fabricacion)
        if ano_fabricacion_entero < 1980:
            raise ValidationError('El año de fabricación debe ser posterior a 1980.')

from django.db import models

class Domicilio(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.ciudad}, {self.provincia}, {self.pais}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.PositiveIntegerField()
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Edad: {self.edad}, Domicilio: {self.domicilio}"



