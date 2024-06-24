from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import ServicoForm, ItemCarrinhoForm, RegistroClienteForm, UserForm
from .models import Servico, Funcionario, ItemCarrinho, Cliente
from django.contrib.auth.decorators import user_passes_test

def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos/lista_servicos.html', {'servicos': servicos})

def adicionar_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_servicos')
    else:
        form = ServicoForm()
    return render(request, 'servicos/adicionar_servico.html', {'form': form})

def adicionar_ao_carrinho(request, servico_id):
    servico = Servico.objects.get(id=servico_id)
    if request.method == 'POST':
        form = ItemCarrinhoForm(request.POST)
        if form.is_valid():
            item_carrinho = form.save(commit=False)
            item_carrinho.servico = servico
            item_carrinho.save()
            return redirect('lista_servicos')
    else:
        form = ItemCarrinhoForm()
    return render(request, 'servicos/adicionar_ao_carrinho.html', {'form': form, 'servico': servico})

def registro_cliente(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        cliente_form = RegistroClienteForm(request.POST)
        if user_form.is_valid() and cliente_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            cliente = cliente_form.save(commit=False)
            cliente.user = user
            cliente.save()
            login(request, user)
            return redirect('area_cliente')
    else:
        user_form = UserForm()
        cliente_form = RegistroClienteForm()
    return render(request, 'servicos/registro_cliente.html', {
        'user_form': user_form,
        'cliente_form': cliente_form
    })

def area_cliente(request):
    cliente = Cliente.objects.get(user=request.user)
    servicos = Servico.objects.filter(cliente=cliente)
    return render(request, 'servicos/area_cliente.html', {'servicos': servicos})


def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def painel_administrador(request):
    return render(request, 'servicos/painel_administrador.html')
