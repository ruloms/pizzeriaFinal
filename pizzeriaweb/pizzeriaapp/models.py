from django.db import models

# Aquí crearemos los modelos

#Modelo para las pizzas
class Pizza(models.Model):

    nombre = models.CharField(max_length=255)
    ingredientes = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='pizzas/%Y/%m/%d', default='pizzas/pizzadef.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.nombre)

#Modelo para los complementos
class Complemento(models.Model):

    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='complementos/%Y/%m/%d', default='complementos/complementodef.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.nombre)

