from django import forms
from .models import MetodosPago
class MetodosPagoForm(forms.ModelForm):
    class Meta:
        model =MetodosPago
        fields = ['nombre_metodo_pago']
        error_messages = {
            'nombre_metodo_pago': {
                'required': '',  # No mostrar texto para el error "required"
            },
        }
        
        
    def clean_nombre_metodo_pago(self):
        nombre_metodo_pago = self.cleaned_data.get('nombre_metodo_pago')
        nombre_metodo_pago = nombre_metodo_pago.upper()
        metodo = MetodosPago.objects.filter(nombre_metodo_pago=nombre_metodo_pago)
        if metodo.exists():
            raise forms.ValidationError("Este metodo de pago ya esta registrado.")
        return nombre_metodo_pago
        