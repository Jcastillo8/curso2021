from django.contrib import admin
from .models import *

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre','marca__marca'] #busquedas
    list_filter = ['marca','estado'] #filtrosdinamicos
    list_display = ['nombre', 'marca', 'fecha_expiracion', 
    'precio', 'existencia','estado'] #columnas
    readonly_fields = ['estado']
    action = ['anular_producto']

	###
	#acciones
	###
    def anular_producto(self, request, queryset):
        for row in queryset.filter(status=True):
            self.log_change(request, row, 'se anula el producto')
        rows_updated = 0
        
        for obj in queryset:
            if obj.estado:
                obj.estado = False
                obj.save()
                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 producto fue anulado"
        else:
            message_bit = "%s productos fueron marcados" % rows_updated
        self.message_user(request, "%s como anulado satisfactoriamente"  % message_bit)
    anular_producto.short_description = 'Anular Producto'


    def activar_producto(self, request, queryset):
        for row in queryset.filter(estado=False):
            self.log_change(request, row, 'Se activa el producto')
        rows_updated = 0
        
        for obj in queryset:
            if obj.estado == False:
                obj.estado = True
                obj.save()
                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 producto fue marcado"
        else:
            message_bit = "%s productos fueron marcados" % rows_updated
        self.message_user(request, "%s como activos satisfactoriamente"  % message_bit)
    activar_producto.short_description = 'Activar Producto'




admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)

