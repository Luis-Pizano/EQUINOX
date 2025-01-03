# Generated by Django 5.0.9 on 2024-12-12 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ejemplares', '0007_alter_ejemplares_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=50)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.cart')),
                ('ejemplar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejemplares.ejemplares')),
            ],
        ),
    ]
