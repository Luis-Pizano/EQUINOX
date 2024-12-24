from django.db import models

from tipo_proveedor.models import TipoProveedor

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    id_tipo_proveedor = models.ForeignKey(TipoProveedor, on_delete=models.CASCADE)
    nombre_proveedor = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    correo = models.EmailField(max_length=255, unique=True)
    
    class Meta:
        db_table = 'proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['id_proveedor'] 

    def __str__(self):
        return f"{self.nombre_proveedor} {self.apellido_paterno} {self.apellido_materno}"