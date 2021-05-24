from django.shortcuts import render
from .models import Pizza, Concesionario

# Create your views here.

def index(request):
    		listaPizzas = Pizza.objects.all()
    		return render(request, 'pizzas/index', {'pizzas':listaPizzas})