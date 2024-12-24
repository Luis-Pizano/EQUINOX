from django.db import models

class Color(models.Model):
    id_color = models.AutoField(primary_key=True)
    nombre_color = models.CharField(max_length=255, unique=True)
    
    class Meta:
        db_table = 'color'
        verbose_name = 'color'
        verbose_name_plural = 'colores'
        ordering = ['id_color']  # Ordena id de menor a mayor

    def __str__(self):
        return self.nombre_color
