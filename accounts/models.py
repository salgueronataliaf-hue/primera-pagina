from django.db import models
from django.contrib.auth.models import User # Importamos el modelo User de Django

class Profile(models.Model):
    # Enlace uno-a-uno con el modelo de Usuario de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Campos adicionales del perfil
    # blank=True y null=True permiten que estos campos no sean obligatorios al inicio
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    
    # Campo de Imagen (Avatar)
    # upload_to='avatars/' guarda las imágenes en media/avatars/
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'
