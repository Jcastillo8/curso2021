from django.contrib import admin
from .models import *

class DetalleVentaInline(admin.TabularInline):  #StackedInline = vertical   TabularInline = horizontal
    model = DetalleVenta # el modelo
    extra = 0 # cantidad de lineas
    #raw.id.fields = ['tipo']
    autocomplete_fields = ['producto']

class VentaAdmin(admin.ModelAdmin):
    inlines = [DetalleVentaInline]
    search_fields = ['cliente__nit', 'cliente__nombre', 'cliente__apellido'] #busquedas
    list_filter = ['fecha_venta', 'empresa', 'empleado'] #filtrosdinamicos
    list_display = ['numero', 'fecha_venta', 'total', 
        'cliente', 'empleado','empresa'] #columnas
    readonly_fields = ['total']
    
admin.site.register(Venta, VentaAdmin)

