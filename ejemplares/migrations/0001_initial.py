# Generated by Django 5.0.9 on 2024-11-26 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
        ('color', '0002_alter_color_options'),
        ('pedigree_ejemplar', '0002_alter_pedigreeejemplar_porcentaje_pureza'),
        ('proveedor', '0002_alter_proveedor_options'),
        ('razas', '0002_alter_razas_imagen'),
        ('sexo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ejemplares',
            fields=[
                ('id_ejemplar', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='static/ejemplares')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.categoria')),
                ('id_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='color.color')),
                ('id_pedigree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedigree_ejemplar.pedigreeejemplar')),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.proveedor')),
                ('id_raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='razas.razas')),
                ('id_sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sexo.sexo')),
            ],
        ),
    ]
