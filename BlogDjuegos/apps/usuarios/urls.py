from django.urls import path
from . import views

app_name = 'usuarios'

#url de la app+
urlpatterns = [
    path('registro/', views.Registro.as_view(), name='registro'),
    
]
