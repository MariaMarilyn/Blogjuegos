from django.shortcuts import render
# Create your views here.
# Importaciones
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistroForm


class Registro(CreateView):
    #forms django 
    form_class = RegistroForm
    success_url =reverse_lazy('login')
    template_name = 'usuarios/registro.html'

# Clara
#from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Resto de las importaciones

class MiLoginView(LoginView):
    template_name = 'usuarios/login.html'
