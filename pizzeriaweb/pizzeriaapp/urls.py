from django.urls import path
from . import views

app_name = 'pizzeriaapp'

urlpatterns = [

 path('', views.index, name='Index'),
 path('about/', views.about, name='About'),
 #path('complementos/', views.lista_complementos, name='Complementos'),
]