from django import forms
from .models import Servico, ItemCarrinho

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome_cliente', 'imagem', 'video', 'audio', 'funcionario']

class ItemCarrinhoForm(forms.ModelForm):
    class Meta:
        model = ItemCarrinho
        fields = ['descricao', 'quantidade']


