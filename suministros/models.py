from django.db import models
from tipo_suministro.models import TipoSuministro
from proveedor.models import Proveedor
from django.core.validators import MinValueValidator


class Suministros(models.Model):
    id_suministro = models.AutoField(primary_key=True)
    id_tipo_suministro = models.ForeignKey(TipoSuministro,on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    nombre_suministro = models.CharField(max_length=255)
    stock = models.IntegerField(validators=[MinValueValidator(0)],default=0)
    traido_el = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'suministros'
        verbose_name = 'Suministro'
        verbose_name_plural = 'Suministros'
        ordering = ['id_suministro'] 

    def __str__(self):
        return self.nombre_suministro