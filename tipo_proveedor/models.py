from django.db import models

class TipoProveedor(models.Model):
    id_tipo_proveedor = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=1,unique=True)
    
    class Meta:
        db_table = 'tipo_proveedor'
        verbose_name = 'Tipo de Proveedor'
        verbose_name_plural = 'Tipos de Proveedores'
        ordering = ['id_tipo_proveedor'] 

    def __str__(self):
        return self.nombre_tipo