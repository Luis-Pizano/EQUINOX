import datetime
from django import forms
from proveedor.models import Proveedor
from .models import Ejemplares

class EjemplaresForm(forms.ModelForm):
    class Meta:
        model = Ejemplares
        fields = ['id_raza', 'id_color', 'id_sexo', 'id_pedigree', 'id_proveedor', 'id_categoria', 'fecha_nacimiento', 'descripcion', 'precio', 'imagen']
        labels = {
            'id_raza': 'Nombre de la Raza',
            'id_color': 'Color',
            'id_sexo': 'Sexo',
            'id_pedigree': 'Pureza',
            'id_proveedor': 'Proveedor',
            'id_categoria': 'Categoria',
            'fecha_nacimiento': 'Fecha de Nacimiento'
        }
        widgets = {
            'precio': forms.NumberInput(attrs={'min': '0'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'min': '1980-01-01', 'max': f'{datetime.datetime.now().year}-12-31'})
        }

    def __init__(self, *args, **kwargs):
        super(EjemplaresForm, self).__init__(*args, **kwargs)
        self.fields['id_proveedor'].queryset = Proveedor.objects.filter(id_tipo_proveedor__nombre_tipo='E')
    
    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if not imagen:
            raise forms.ValidationError('Por favor suba una imagen.')
        return imagen
    
    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < 0:
            raise forms.ValidationError('El precio no puede ser menor a 0.')
        return precio
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')  # Obtén el valor del campo
        if descripcion:  # Asegúrate de que no sea None
            descripcion = descripcion.upper()  # Convierte a mayúsculas
        return descripcion


class EjemplaresEditForm(forms.ModelForm):
    class Meta:
        model = Ejemplares
        fields = ['precio', 'descripcion', 'id_categoria', 'id_pedigree','id_color','imagen']
        labels = {
            'id_categoria': 'Categoría',
            'id_pedigree': 'Pureza',  
            'id_color': 'Color',  
            'descripcion': 'descripcion',  
        }
        error_messages = {
            'id_categoria': {
                'required': '',  # No mostrar texto para el error "required"
            },
            'id_pedigree': {
                'required': '',  # No mostrar texto para el error "required"
            },
            'id_color': {
                'required': '',  # No mostrar texto para el error "required"
            },
            'precio': {
                'required': '',  # No mostrar texto para el error "required"
            },
            'descripcion': {
                'required': '',  # No mostrar texto para el error "required"
            },
            
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_categoria'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_pedigree'].widget.attrs.update({'class': 'form-control'})
        self.fields['precio'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Precio del ejemplar'})
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')  # Obtén el valor del campo
        if descripcion:  # Asegúrate de que no sea None
            descripcion = descripcion.upper()  # Convierte a mayúsculas
        return descripcion
