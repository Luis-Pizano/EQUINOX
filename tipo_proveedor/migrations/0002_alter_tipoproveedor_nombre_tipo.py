# Generated by Django 5.0.9 on 2024-11-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipo_proveedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoproveedor',
            name='nombre_tipo',
            field=models.CharField(max_length=1, unique=True),
        ),
    ]
