# Generated by Django 3.2.3 on 2021-05-21 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0007_rename_tipo_telefono_tipo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelOptions(
            name='telefono',
            options={'verbose_name': 'Telefono de Empleado', 'verbose_name_plural': 'Telefonos de Empleados'},
        ),
        migrations.AlterModelTable(
            name='empleado',
            table='empleado',
        ),
    ]