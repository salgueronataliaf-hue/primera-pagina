# CÓDIGO COMPLETO PARA blog/models.py 
from django.db import models

# 1. Modelo Autor (Clase 1)
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# 2. Modelo Categoria (Clase 2)
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

# 3. Modelo Post (Clase 3)
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255, blank=True, null=True) 
    contenido = models.TextField() 
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) 
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

# Create your models here.
