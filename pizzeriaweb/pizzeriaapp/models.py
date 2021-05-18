from django.db import models

# Create your models here.

class Pizza(models.Model):
    nombre = models.CharField(max_length=25, db_Index=True)
    ingredientes = models.CharField(max_length=100, db_Index=True)
    foto = models.ImageField(upload_to='pizzas/%Y/%m/%d', default='pizzas/pizzadef.jpg')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(self.nombre)

class Complemento(models.Model):
    nombre = models.CharField(max_length=25, db_Index=True)
    descripcion = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='complementos/%Y/%m/%d', default='complementos/complementodef.png')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(self.nombre)

