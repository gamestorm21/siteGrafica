from django.contrib import admin
from .models import Funcionario, Servico, ItemCarrinho, Cliente

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'funcionario', 'imagem', 'video', 'audio')
    list_filter = ('funcionario',)
    search_fields = ('nome_cliente', 'funcionario__nome')

class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'descricao', 'quantidade')
    list_filter = ('servico',)
    search_fields = ('descricao',)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'user')
    search_fields = ('nome', 'user__username')

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(ItemCarrinho, ItemCarrinhoAdmin)
admin.site.register(Cliente, ClienteAdmin)
