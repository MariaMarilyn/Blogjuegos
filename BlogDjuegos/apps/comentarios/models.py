from django.db import models

# Create your models here.
from apps.posts.models import Post
from django.db import models
from ckeditor.fields import RichTextField

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    contenido = RichTextField()

    def __str__(self):
        return f"Comentario en {self.post.titulo}"
