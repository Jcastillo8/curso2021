# Generated by Django 3.2.3 on 2021-05-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0003_empleado_dpi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='dpi',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='DPI'),
        ),
    ]
