# Generated by Django 5.0.9 on 2024-11-26 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplares', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ejemplares',
            options={'ordering': ['id_ejemplar'], 'verbose_name': 'ejemplar', 'verbose_name_plural': 'ejemplares'},
        ),
    ]
