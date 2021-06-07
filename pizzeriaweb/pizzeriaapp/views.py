from django.shortcuts import render
from .models import Pizza, Complemento

# Create your views here.

def index(request):
    		listaPizzas = Pizza.objects.all()
    		return render(request, 'index.html', {'pizzas':listaPizzas})