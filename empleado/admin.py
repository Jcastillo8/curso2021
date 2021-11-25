# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *

class TelefonoInline(admin.TabularInline):  #StackedInline = vertical	TabularInline = horizontal
    model = Telefono # el modelo
    extra = 0 # cantidad de lineas
    #raw.id.fields = ['tipo']
    autocomplete_fields = ['tipo']  

class EmpleadoAdmin(admin.ModelAdmin):
    inlines = [TelefonoInline] #Detalles dentro del modelo
    search_fields = ['nombre','apellido','telefono'] #busquedas
    list_filter = ['genero','fecha_nacimiento'] #filtrosdinamicos
    list_display = ['dpi','nombre', 'genero','apellido', 'fecha_nacimiento', 'edad', 'correo'] #columnas

admin.site.register(Empleado, EmpleadoAdmin)
