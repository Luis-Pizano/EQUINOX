# Generated by Django 5.0.9 on 2024-10-27 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='first_name',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='last_name',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='phone_number',
            new_name='numero_telefono',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='username',
            new_name='usuario',
        ),
    ]