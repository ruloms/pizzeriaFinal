from django.shortcuts import render
from .models import Pizza, Complemento

# Create your views here.

def index(request):
    listaPizzas = Pizza.objects.all()
    return render(request, 'index.html', {'pizzas':listaPizzas})

def about(request):
    listaPizzas = Pizza.objects.all()
    return render(request, 'about.html', {'pizzas':listaPizzas})

def menu(request):
    listaPizzas = Pizza.objects.all()
    listaComplementos = Complemento.objects.all()
    return render(request, 'menu.html', {'pizzas':listaPizzas, 'complementos':listaComplementos})

def gallery(request):
    listaPizzas = Pizza.objects.all()
    return render(request, 'gallery.html', {'pizzas':listaPizzas})

def blog(request):
    listaPizzas = Pizza.objects.all()
    return render(request, 'blog.html', {'pizzas':listaPizzas})

def reservations(request):
    listaPizzas = Pizza.objects.all()
    return render(request, 'reservations.html', {'pizzas':listaPizzas})