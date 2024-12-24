# Generated by Django 5.0.9 on 2024-11-28 15:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplares', '0002_alter_ejemplares_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejemplares',
            name='precio',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]