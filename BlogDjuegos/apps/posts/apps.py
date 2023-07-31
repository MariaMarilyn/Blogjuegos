from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.posts'
# Lo mismo, solo cambios para subir a git hub porque no podemos hacer merge