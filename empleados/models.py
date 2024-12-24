from django.db import models
from tipo_empleado.models import TipoEmpleado

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    id_tipo_empleado = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    nombre_empleado = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    correo = models.EmailField(max_length=255, unique=True)

    class Meta:
        db_table = 'empleados'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f"{self.nombre_empleado} {self.apellido_paterno} {self.apellido_materno}"

