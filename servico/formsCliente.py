from django import forms
from django.contrib.auth.models import User
from .models import Servico, ItemCarrinho, Cliente

class RegistroClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }
