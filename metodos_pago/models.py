from django.db import models

class MetodosPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    nombre_metodo_pago = models.CharField(max_length=255, blank=False)
    
    class Meta:
        db_table = 'metodos_pago'
        verbose_name = 'metodo_pago'
        verbose_name_plural = 'metodos_pago'
        
    def __str__(self):
        return self.nombre_metodo_pago