from django.urls import path
from . import views

app_name = 'pizzeriaapp'

urlpatterns = [

 path('', views.index, name='Index'),
 path('about/', views.about, name='About'),
 path('menu/', views.menu, name='Menu'),
 path('pizzas/', views.gallery, name='Pizzas'),
 path('blog/', views.blog, name='Blog'),
 path('contact/', views.reservations, name='Contact'),
]