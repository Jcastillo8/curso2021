from django.contrib import admin
from .models import*

class TipoTelefonoAdmin(admin.ModelAdmin):
    search_fields = ['tipo'] #busquedas


admin.site.register(TipoTelefono, TipoTelefonoAdmin)
# Register your models here.
