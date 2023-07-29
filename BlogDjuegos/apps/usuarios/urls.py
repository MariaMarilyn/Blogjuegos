from django.urls import path
from . import views

app_name = 'usuarios'

#url de la app+
urlpatterns = [
    #path('registro/', views.Registro.as_view(), name='registro'),
    
]

#Clara- usuarios/urls.py
#from django.urls import path
from .views import Registro, LoginView

urlpatterns = [
    path('registro/', Registro.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
]
