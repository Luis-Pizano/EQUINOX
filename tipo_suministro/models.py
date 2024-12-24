from django.db import models

class TipoSuministro(models.Model):
    id_tipo_suministro = models.AutoField(primary_key=True)
    nombre_suministro = models.CharField(max_length=255,unique=True)
    
    class Meta:
        db_table = 'tipo_suministro'
        verbose_name = 'Tipo de Suministro'
        verbose_name_plural = 'Tipos de Suministros'
        ordering = ['id_tipo_suministro'] 

    def __str__(self):
        return self.nombre_suministro