from django import forms
from .models import Razas
from django.core.exceptions import ValidationError

class RazasForm(forms.ModelForm):
    class Meta:
        model = Razas
        fields = ['nombre_raza','imagen']
        
        
    def clean_nombre_raza(self):
        nombre_raza = self.cleaned_data.get('nombre_raza')
        nombre_raza = nombre_raza.upper()
        raza =Razas.objects.filter(nombre_raza=nombre_raza)
        if raza.exists():
            raise ValidationError("Esta raza ya esta registrada.")
        return nombre_raza
    
class RazasFormEditar(forms.ModelForm):
    class Meta(RazasForm.Meta):
        fields = ['nombre_raza']
        error_messages = {
            'nombre_raza': {
                'required': '',  # No mostrar texto para el error "required"
            },
        }

    def clean_nombre_raza(self):
        nombre_raza = self.cleaned_data.get('nombre_raza').upper()
        # Cambiamos 'id' por 'id_raza'
        raza = Razas.objects.filter(nombre_raza=nombre_raza).exclude(id_raza=self.instance.id_raza)
        if raza.exists():
            raise ValidationError("Esta raza ya está registrada.")
        return nombre_raza
