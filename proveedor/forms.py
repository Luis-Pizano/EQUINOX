from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_proveedor', 'apellido_paterno', 'apellido_materno', 'correo', 'id_tipo_proveedor']
        labels = {
            'id_tipo_proveedor': 'Tipo de Proveedor'
        }

    def clean(self):
        cleaned_data = super().clean()

        if 'nombre_proveedor' in cleaned_data:
            cleaned_data['nombre_proveedor'] = cleaned_data['nombre_proveedor'].upper()

        if 'apellido_paterno' in cleaned_data:
            cleaned_data['apellido_paterno'] = cleaned_data['apellido_paterno'].upper()

        if 'apellido_materno' in cleaned_data:
            cleaned_data['apellido_materno'] = cleaned_data['apellido_materno'].upper()

        return cleaned_data
    
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        correo_existente = Proveedor.objects.filter(correo=correo)
        if correo_existente.exists():
            raise forms.ValidationError("Este correo ya ha sido registrado.")
        return correo

    