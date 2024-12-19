from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['id_tipo_empleado', 'nombre_empleado', 'apellido_paterno', 'apellido_materno', 'correo']
        labels = {
            'id_tipo_empleado':'Tipo de empleado'
        }
        error_messages = {
            'id_tipo_empleado': {
                'required': '',  # No mostrar texto para el error "required"
            },
            'nombre_empleado': {
                'required': '',  # No mostrar texto para el error "required"
            },
            'apellido_paterno': {
                'required': '',  # No mostrar texto para el error "required"
            },
            'apellido_materno': {
                'required': '',  # No mostrar texto para el error "required"
            },
            'correo': {
                'required': '',  # No mostrar texto para el error "required"
            },
        }

    def clean(self):
        cleaned_data = super().clean()

        # Convertir los campos a mayúsculas
        if 'nombre_empleado' in cleaned_data:
            cleaned_data['nombre_empleado'] = cleaned_data['nombre_empleado'].upper()

        if 'apellido_paterno' in cleaned_data:
            cleaned_data['apellido_paterno'] = cleaned_data['apellido_paterno'].upper()

        if 'apellido_materno' in cleaned_data:
            cleaned_data['apellido_materno'] = cleaned_data['apellido_materno'].upper()

        return cleaned_data
