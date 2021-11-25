# -*- coding: utf-8 -*-
from django.db import models
from comun.models import Persona, TipoTelefono

class Empleado(Persona):
    dpi = models.CharField('DPI', max_length=14, null=True, blank=True)

    class Meta():
        db_table = 'empleado'
        verbose_name= 'Empleado'
        verbose_name_plural = 'Empleados'

class Telefono(models.Model):
    empleado = models.ForeignKey(
        Empleado, verbose_name='Empleado', on_delete=models.CASCADE)
    numero = models.PositiveIntegerField(
        'numero de telefono', help_text='solo incluir numeros' 
    )
    tipo =models.ForeignKey(
        TipoTelefono, verbose_name='Tipo telefono', on_delete=models.CASCADE)
    def __str_(self):
        return "%s : %s" % (self.empleado, self.numero)

    class Meta():
        verbose_name= 'Telefono de Empleado'
        verbose_name_plural = 'Telefonos de Empleados'



