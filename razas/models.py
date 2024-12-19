from django.db import models

class Razas(models.Model):
    id_raza = models.AutoField(primary_key=True)
    nombre_raza = models.CharField(max_length=255, unique=True)
    imagen = models.ImageField(upload_to='images/razas', blank=False)
    
    
    class Meta:
        db_table = 'razas'
        verbose_name = 'raza'
        verbose_name_plural = 'razas'
        
    def __str__(self):
        return self.nombre_raza