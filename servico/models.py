from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome_cliente = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    audio = models.FileField(upload_to='audios/', blank=True, null=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Serviço para {self.nome_cliente} por {self.funcionario.nome}"

class ItemCarrinho(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.descricao


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
