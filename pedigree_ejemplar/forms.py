from django import forms
from .models import PedigreeEjemplar
from django.core.exceptions import ValidationError

class PedigreeEjemplarForm(forms.ModelForm):
    class Meta:
        model = PedigreeEjemplar
        fields = ['porcentaje_pureza', 'descripcion']
        widgets = {
            'porcentaje_pureza': forms.NumberInput(attrs={'min': '0', 'max': '100'}) }
    
    def clean_porcentaje_pureza(self):
        porcentaje_pureza = self.cleaned_data['porcentaje_pureza']
        if porcentaje_pureza < 0:
            raise ValidationError('El porcentaje de pureza no puede ser menor a 0.')
        if porcentaje_pureza > 100:
            raise ValidationError('El porcentaje de pureza no puede ser mayor a 100.')
        return porcentaje_pureza

