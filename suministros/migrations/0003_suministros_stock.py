# Generated by Django 5.0.9 on 2024-11-28 15:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suministros', '0002_alter_suministros_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='suministros',
            name='stock',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
