from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    groups = models.ManyToManyField('auth.Group', related_name='usuarios')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='usuarios')

#Aca tube que utilizar you.com que es una IA para modificar el codigo porque me tiraba este error 

#ERRORS:
#auth.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'auth.User.groups' 
# clashes with reverse accessor for 'usuarios.Usuario.groups'.
#        HINT: Add or change a related_name argument to the definition for 'auth.User.groups' or
#  'usuarios.Usuario.groups'.
#auth.User.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 'auth.User.user_permissions'
#  clashes with reverse accessor for 'usuarios.Usuario.user_permissions'.
#        HINT: Add or change a related_name argument to the definition for 'auth.User.user_permissions' or
#  'usuarios.Usuario.user_permissions'.
#usuarios.Usuario.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'usuarios.Usuario.groups'
#  clashes with reverse accessor for 'auth.User.groups'.
#        HINT: Add or change a related_name argument to the definition for 'usuarios.Usuario.groups' or 
# 'auth.User.groups'.
#usuarios.Usuario.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for
#  'usuarios.Usuario.user_permissions' clashes with reverse accessor for 'auth.User.user_permissions'.
#        HINT: Add or change a related_name argument to the definition for 'usuarios.Usuario.user_permissions'
#  or 'auth.User.user_permissions'.