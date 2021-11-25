# -*- coding: utf-8 -*-
from django.db import models
from comun.models import Persona, TipoTelefono

class Cliente(Persona):
    nit = models.CharField('NIT', max_length=10, unique=True)

    def __str__(self):
        return '%s: %s, %s' % (self.nit, self.apellido, self.nombre)

    class Meta():
        db_table = 'cliente'
        verbose_name= 'Cliente'
        verbose_name_plural = 'Clientes'

class Telefono(models.Model):
    cliente = models.ForeignKey(
        Cliente, verbose_name='Cliente', on_delete=models.CASCADE)
    numero = models.PositiveIntegerField(
        'numero de telefono', help_text='solo incluir numeros' 
    )
    tipo =models.ForeignKey(
        TipoTelefono, verbose_name='Tipo telefono',related_name='TelCliente', on_delete=models.CASCADE)
    
    def __str_(self):
        return "%s : %s" % (self.cliente, self.numero)

    class Meta():
        verbose_name= 'Telefono de cliente'
        verbose_name_plural = 'Telefonos de Clientes'