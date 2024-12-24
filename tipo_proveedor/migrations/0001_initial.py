# Generated by Django 5.0.9 on 2024-11-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProveedor',
            fields=[
                ('id_tipo_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de Proveedor',
                'verbose_name_plural': 'Tipos de Proveedores',
            },
        ),
    ]