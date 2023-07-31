from django.shortcuts import render

def login(request):
    context = {
        }
    return render(request, r'usuarios/login.html', context)

def register(request):
    context = {
        }
    return render(request, r'usuarios/registro.html', context)