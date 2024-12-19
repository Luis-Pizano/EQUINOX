from django.db import models
from empleados.models import Empleado
from clientes.models import Clientes
from ejemplares.models import Ejemplares
from metodos_pago.models import MetodosPago

class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado,on_delete=models.PROTECT)
    id_cliente = models.ForeignKey(Clientes,on_delete=models.PROTECT)
    id_ejemplar = models.ForeignKey(Ejemplares,on_delete=models.PROTECT)
    id_metodo_pago = models.ForeignKey(MetodosPago,on_delete=models.PROTECT)
    fecha = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'ventas'
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['fecha']
    
    def __str__(self):
        return f'{self.id_venta}-{self.id_empleado}-{self.id_cliente}-{self.id_ejemplar}'