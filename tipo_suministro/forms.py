from django import forms
from .models import TipoSuministro

class TipoSuministroForm(forms.ModelForm):
    class Meta:
        model = TipoSuministro
        fields = ['nombre_suministro']
        error_messages = {
            'nombre_suministro': {
                'required': '', 
            },
        }
        
    def clean_nombre_suministro(self):
        nombre_suministro = self.cleaned_data.get('nombre_suministro')
        nombre_suministro = nombre_suministro.upper()
        tipo_suministro =TipoSuministro.objects.filter(nombre_suministro=nombre_suministro)
        if tipo_suministro.exists():
            raise forms.ValidationError("Este tipo de suministro ya ha sido registrado.")
        return nombre_suministro