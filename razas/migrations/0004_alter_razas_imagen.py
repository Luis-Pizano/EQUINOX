# Generated by Django 5.0.9 on 2024-12-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razas', '0003_alter_razas_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='razas',
            name='imagen',
            field=models.ImageField(upload_to='images/razas'),
        ),
    ]