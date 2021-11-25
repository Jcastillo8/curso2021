# -*- coding: utf-8 -*-

from django.contrib import admin
from.models import *

class TelefonoInline(admin.TabularInline):  #StackedInline = vertical	TabularInline = horizontal
    model = Telefono # el modelo
    extra = 0 # cantidad de lineas
    #raw.id.fields = ['tipo']
    autocomplete_fields = ['tipo']

class ClienteAdmin(admin.ModelAdmin):
    inlines = [TelefonoInline]
    search_fields = ['nombre','apellido'] #busquedas
    list_filter = ['genero','fecha_nacimiento'] #filtrosdinamicos
    list_display = ['nit','nombre', 'apellido', 'fecha_nacimiento', 'edad'  ] #columnas

admin.site.register(Cliente, ClienteAdmin)