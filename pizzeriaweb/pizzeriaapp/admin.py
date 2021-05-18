from django.contrib import admin
from .models import Pizza, Complemento

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'ingredientes', 'updated']
    list_filter = ['nombre', 'ingredientes']
    fields = ('nombre', 'ingredientes', 'foto')    
    search_fields = ('nombre', 'ingredientes')
    

    def get_queryset(self, request):
        return super(PizzaAdmin, self).get_queryset(request).order_by('-updated')

@admin.register(Complemento)
class ComplementoAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'descripcion', 'updated']
    list_filter = ['nombre', 'descripcion']
    fields = ('nombre', 'descripcion', 'foto')    
    search_fields = ('nombre', 'descripcion')
    

    def get_queryset(self, request):
        return super(ComplementoAdmin, self).get_queryset(request).order_by('-updated')