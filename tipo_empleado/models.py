from django.db import models

class TipoEmpleado(models.Model):
    id_tipo_empleado = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'tipo_empleado'  
        verbose_name = 'Tipo de Empleado'
        verbose_name_plural = 'Tipos de Empleados'

    def __str__(self):
        return self.nombre_tipo
