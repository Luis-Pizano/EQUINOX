from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class PedigreeEjemplar(models.Model):
    id_pedigree = models.AutoField(primary_key=True)
    porcentaje_pureza = models.IntegerField(unique=True,validators=[MaxValueValidator(100), MinValueValidator(0)])
    descripcion = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'pedigree_ejemplar'
        verbose_name = 'pedigree_ejemplar'
        verbose_name_plural = 'pedigree_ejemplares'
        ordering = ['id_pedigree'] 

    def __str__(self):
        return f"{self.porcentaje_pureza}%" 