from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='posts/', blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
