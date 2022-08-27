from django.db import models
from datetime import datetime

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=150)
    cpf = models.CharField('CPF', max_length=20)
    data_nascimento = models.DateField('Data de Nascimento')
    telefone = models.CharField('Telefone', max_length=15)
    email = models.EmailField('Email', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    modelo = models.CharField('Modelo', max_length=150)
    marca = models.CharField('Marca', max_length=20)
    ano = models.IntegerField()
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=7)
    pessoa = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.placa

class Produto(models.Model):
    nome_produto = models.CharField('Produto', max_length=500)
    preco = models.FloatField()
    descricao = models.TextField()
    pessoa = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome_produto

class Imagem(models.Model):
    imagem = models.ImageField()

class Protocolo(models.Model):
    protocolo = models.CharField(max_length=8)
    pessoa = models.ForeignKey(Cliente, models.DO_NOTHING)

    def __str__(self):
        return f'Protocolo de {self.pessoa.nome}'
    
class Servico(models.Model):
    nome_servico = models.CharField('Servico', max_length=500)
    preco = models.FloatField()
    descricao = models.TextField()
    protocolo = models.ForeignKey(Protocolo, on_delete=models.DO_NOTHING)
    imagem = models.ForeignKey(Imagem, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_servico

