from django.utils import timezone  
from django.db import models
from razas.models import Razas
from color.models import Color
from sexo.models import Sexo
from pedigree_ejemplar.models import PedigreeEjemplar
from proveedor.models import Proveedor
from categorias.models import Categoria
from django.core.validators import MinValueValidator
from django.utils.formats import number_format

class Ejemplares(models.Model):
    id_ejemplar = models.AutoField(primary_key=True)
    id_raza = models.ForeignKey(Razas,on_delete=models.CASCADE)
    id_color = models.ForeignKey(Color,on_delete=models.CASCADE)
    id_sexo = models.ForeignKey(Sexo,on_delete=models.CASCADE)
    id_pedigree = models.ForeignKey(PedigreeEjemplar,on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=False, default=timezone.now)
    descripcion = models.CharField(max_length=2555, blank=False, null=False)
    precio = models.IntegerField(null=False, blank=False,validators=[MinValueValidator(0)],default=0)
    imagen = models.ImageField(upload_to='images/ejemplares', blank=False)

    
    class Meta:
        db_table = 'ejemplares'
        verbose_name = 'ejemplar'
        verbose_name_plural = 'ejemplares'
        ordering = ['id_ejemplar'] 
    
    def __str__(self):
     return f"{self.id_ejemplar}-{self.id_pedigree}"

    def precio_formateado(self):
        return f"{self.precio:,.0f}".replace(",", ".")