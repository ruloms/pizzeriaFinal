from django.contrib import admin
from .models import Pizza, Complemento

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'ingredientes', 'precio_individual', 'precio_mediana', 'precio_familiar', 'updated', 'foto']
    list_filter = ['nombre', 'ingredientes', 'precio_individual', 'precio_mediana', 'precio_familiar', 'foto']
    fields = ('nombre', 'ingredientes', 'precio_individual', 'precio_mediana', 'precio_familiar', 'foto')    
    search_fields = ('nombre', 'ingredientes')
    

    def get_queryset(self, request):
        return super(PizzaAdmin, self).get_queryset(request).order_by('-updated')

@admin.register(Complemento)
class ComplementoAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'descripcion', 'precio', 'updated']
    list_filter = ['nombre', 'descripcion', 'precio']
    fields = ('nombre', 'descripcion', 'precio', 'foto')    
    search_fields = ('nombre', 'descripcion')
    

    def get_queryset(self, request):
        return super(ComplementoAdmin, self).get_queryset(request).order_by('-updated')