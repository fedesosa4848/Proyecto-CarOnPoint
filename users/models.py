from django.db import models
from django.contrib.auth.models import User

class DataUserExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)
    about_me = models.TextField(default='', blank=True, null=False)  # Agregar un valor predeterminado

    def __str__(self):
        return f'Perfil de {self.user.username}'
