from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=255,unique=True)
    
    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id_categoria'] 

    def __str__(self):
        return self.nombre_categoria
