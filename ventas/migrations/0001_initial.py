# Generated by Django 5.0.9 on 2024-11-28 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0002_alter_clientes_options'),
        ('ejemplares', '0003_ejemplares_precio'),
        ('empleados', '0003_alter_empleado_table'),
        ('metodos_pago', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes.clientes')),
                ('id_ejemplar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ejemplares.ejemplares')),
                ('id_empleado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empleados.empleado')),
                ('id_metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='metodos_pago.metodospago')),
            ],
        ),
    ]