# Generated by Django 5.0.9 on 2024-11-22 20:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PedigreeEjemplar',
            fields=[
                ('id_pedigree', models.AutoField(primary_key=True, serialize=False)),
                ('porcentaje_pureza', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(100)])),
                ('descripcion', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'pedigree_ejemplar',
                'verbose_name_plural': 'pedigree_ejemplares',
                'ordering': ['id_pedigree'],
            },
        ),
    ]