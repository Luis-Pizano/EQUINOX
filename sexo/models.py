from django.db import models

class Sexo(models.Model):
    id_sexo = models.AutoField(primary_key=True)
    nombre_sexo = models.CharField(max_length=6,unique=True)
    
    class Meta:
        db_table = 'sexo'
        verbose_name = 'sexo'
        verbose_name_plural = 'sexos'
        ordering = ['id_sexo']
        
    def __str__(self):
        return self.nombre_sexo