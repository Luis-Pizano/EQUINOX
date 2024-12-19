from django import forms

from .models import Clientes

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre_cliente','apellido_paterno','apellido_materno','correo']
        
            
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        # Verificar que el correo no esté registrado, pero permitirlo si pertenece al mismo cliente
        if correo:
            cliente_id = self.instance.id_cliente  # Obtenemos el id del cliente editado
            correo_existente = Clientes.objects.filter(correo=correo).exclude(id_cliente=cliente_id)
            if correo_existente.exists():
                raise forms.ValidationError("Este correo ya está registrado.")
        return correo

    def clean_nombre_cliente(self):
        nombre_cliente = self.cleaned_data.get('nombre_cliente')
        return nombre_cliente.upper()

    def clean_apellido_paterno(self):
        apellido_paterno = self.cleaned_data.get('apellido_paterno')
        return apellido_paterno.upper()

    def clean_apellido_materno(self):
        apellido_materno = self.cleaned_data.get('apellido_materno')
        return apellido_materno.upper()
    
    
class ClientesFormEditar(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre_cliente','apellido_paterno','apellido_materno','correo']
        error_messages = {
            'nombre_cliente': {
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
        
            
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        # Verificar que el correo no esté registrado, pero permitirlo si pertenece al mismo cliente
        if correo:
            cliente_id = self.instance.id_cliente  # Obtenemos el id del cliente editado
            correo_existente = Clientes.objects.filter(correo=correo).exclude(id_cliente=cliente_id)
            if correo_existente.exists():
                raise forms.ValidationError("Este correo ya está registrado.")
        return correo

    def clean_nombre_cliente(self):
        nombre_cliente = self.cleaned_data.get('nombre_cliente')
        return nombre_cliente.upper()

    def clean_apellido_paterno(self):
        apellido_paterno = self.cleaned_data.get('apellido_paterno')
        return apellido_paterno.upper()

    def clean_apellido_materno(self):
        apellido_materno = self.cleaned_data.get('apellido_materno')
        return apellido_materno.upper()