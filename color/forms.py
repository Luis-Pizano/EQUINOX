from django import forms
from .models import Color

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ["nombre_color"]
        
    def clean_nombre_color(self):
        nombre_color = self.cleaned_data.get('nombre_color')
        nombre_color = nombre_color.upper()
        color = Color.objects.filter(nombre_color=nombre_color)
        if color.exists():
            raise forms.ValidationError("Este color ya esta registrado.")
        return nombre_color
