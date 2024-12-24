from django import forms
from .models import Account

class RegistarseForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    numero_telefono = forms.CharField(max_length=9, label='Número de Teléfono')

    class Meta:
        model = Account
        fields = ['nombre', 'apellido', 'email', 'numero_telefono', 'usuario', 'password']
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Este campo no puede estar vacío")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Encripta la contraseña
        if commit:
            user.save()
        return user


