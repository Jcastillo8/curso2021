# Generated by Django 3.2.3 on 2021-05-21 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0006_telefono_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telefono',
            old_name='Tipo',
            new_name='tipo',
        ),
    ]