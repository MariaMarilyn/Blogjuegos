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

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('nombre_de_la_vista_principal')  # Cambiar por la vista principal de tu blog de juegos
            else:
                messages.error(request, 'Credenciales inválidas. Inténtalo nuevamente.')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
