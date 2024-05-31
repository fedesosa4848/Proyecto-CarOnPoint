from django.db import models

class Vehiculo(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
