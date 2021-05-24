from django.urls import path
from . import views

app_name = 'pizzeriaapp'

urlpatterns = [

 path('', views.index, name='Index'),
 path('pizzas', views.lista_vehiculos, name='Pizzas'),
 path('complementos/', views.lista_concesionarios, name='Complementos'),
]