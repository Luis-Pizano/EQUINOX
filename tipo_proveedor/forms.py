from django import forms
from .models import TipoProveedor

class TipoProveedorForm(forms.ModelForm):
    class Meta:
        model = TipoProveedor
        fields = ['nombre_tipo']
        
    def clean_nombre_tipo(self):
        nombre_tipo = self.cleaned_data.get('nombre_tipo')
        nombre_tipo = nombre_tipo.upper()
        tipo_proveedor = TipoProveedor.objects.filter(nombre_tipo=nombre_tipo)
        if tipo_proveedor.exists():
            raise forms.ValidationError("Este tipo de proveedor ya ha sido registrado.")
        return nombre_tipo
