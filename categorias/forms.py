from .models import Categoria
from django import forms

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre_categoria']
        error_messages = {
            'nombre_categoria': {
                'required': '',
            },
        }
        
    def clean_nombre_categoria(self):
        nombre_categoria = self.cleaned_data.get('nombre_categoria')
        nombre_categoria = nombre_categoria.upper()
        categoria = Categoria.objects.filter(nombre_categoria=nombre_categoria)
        if categoria.exists():
            raise forms.ValidationError("Esta categoria ya ha sido registrado.")
        return nombre_categoria