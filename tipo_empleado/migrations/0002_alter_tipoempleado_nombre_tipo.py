# Generated by Django 5.0.9 on 2024-11-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipo_empleado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoempleado',
            name='nombre_tipo',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]