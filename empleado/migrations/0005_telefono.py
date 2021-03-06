# Generated by Django 3.2.3 on 2021-05-20 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0004_alter_empleado_dpi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(help_text='solo incluir numeros', verbose_name='numero de telefono')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado', verbose_name='Empleado')),
            ],
        ),
    ]
