from django import forms
from .models import Sexo
from django.core.exceptions import ValidationError

class SexoForm(forms.ModelForm):
    class Meta:
        model = Sexo
        fields = ["nombre_sexo"]

    def clean_nombre_sexo(self):
        nombre_sexo = self.cleaned_data.get('nombre_sexo')
        nombre_sexo = nombre_sexo.upper()
        sexo = Sexo.objects.filter(nombre_sexo=nombre_sexo)
        if sexo.exists():
            raise forms.ValidationError("Este sexo ya esta registrado.")
        return nombre_sexo
