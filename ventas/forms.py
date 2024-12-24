from django import forms
from .models import Ventas
from ejemplares.models import Ejemplares

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ['id_empleado','id_cliente','id_ejemplar','id_metodo_pago']
        labels = {
            'id_empleado':'Empleado',
            'id_cliente':'Cliente',
            'id_ejemplar':'Ejemplar',
            'id_metodo_pago':'Metodo de pago',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar ejemplares que no están asociados a una venta existente
        ejemplares_usados = Ventas.objects.values_list('id_ejemplar', flat=True)
        self.fields['id_ejemplar'].queryset = Ejemplares.objects.exclude(id_ejemplar__in=ejemplares_usados) #se exclukye los ejemplares de la lista select id_ejemplar que fueron usados en ventas
        
        # doble guion bajo __ es como si fuera un like de SQL