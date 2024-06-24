from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_servicos, name='lista_servicos'),
    path('adicionar/', views.adicionar_servico, name='adicionar_servico'),
    path('adicionar_ao_carrinho/<int:servico_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('registro/', views.registro_cliente, name='registro_cliente'),
    path('area_cliente/', views.area_cliente, name='area_cliente'),
    path('painel_administrador/', views.painel_administrador, name='painel_administrador'),
]
