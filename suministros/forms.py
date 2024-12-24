from django import forms
from .models import Suministros, Proveedor 
from django.core.exceptions import ValidationError

class SuministrosForm(forms.ModelForm):
    class Meta:
        model = Suministros
        fields = ['id_tipo_suministro', 'id_proveedor', 'nombre_suministro','stock']
        labels = {
            'id_tipo_suministro':'Tipo de suministro',
            'id_proveedor':'Proveedor',
            'stock':'Cantidad'
        }
        widgets = {
            'stock': forms.NumberInput(attrs={'min': '0'}) }

    def __init__(self, *args, **kwargs):
        super(SuministrosForm, self).__init__(*args, **kwargs)
        
        # Filtrar el queryset de proveedores para mostrar solo los de tipo 'S'
        self.fields['id_proveedor'].queryset = Proveedor.objects.filter(id_tipo_proveedor__nombre_tipo='S')

    def clean_nombre_suministro(self):
        nombre_suministro = self.cleaned_data.get('nombre_suministro')
        if nombre_suministro:
            nombre_suministro = nombre_suministro.upper()
        return nombre_suministro
    
    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock < 0:
            raise ValidationError('El stock no puede ser menor a 0.')
        return stock

class SuministroEditForm(forms.ModelForm):
    class Meta:
        model = Suministros
        fields = ['stock']  # Solo el campo stock es editable
        error_messages = {
            'stock': {
                'required': '',  # No mostrar texto para el error "required"
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Stock'})