from django.db import models

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    correo = models.EmailField(max_length=255, unique=True)
    
    
    class Meta:
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id_cliente'] 

    def __str__(self):
        return f'{self.nombre_cliente} {self.apellido_paterno} {self.apellido_materno}'