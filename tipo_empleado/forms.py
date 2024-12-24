from django import forms
from .models import TipoEmpleado

class TipoEmpleadoForm(forms.ModelForm):
    class Meta:
        model = TipoEmpleado
        fields = ['nombre_tipo']
        error_messages = {
            'nombre_tipo': {
                'required': '',  # Mensaje vacío para no mostrar texto
            },
        }
         
        
    def clean_nombre_tipo(self):
        nombre_tipo = self.cleaned_data.get('nombre_tipo')
        nombre_tipo = nombre_tipo.upper()
        tipo_empleado = TipoEmpleado.objects.filter(nombre_tipo=nombre_tipo)
        if tipo_empleado.exists():
            raise forms.ValidationError("Este tipo de empleado ya ha sido registrado.")
        return nombre_tipo
