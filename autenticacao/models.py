from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.Charfield('Nome', max_length=150)
    cpf = models.CharField('CPF', max_length=20)
    data_nascimento = models.DateField('Data de Nascimento')
    telefone = models.CharField('Telefone', max_length=15)
    email = models.EmailField('Email', max_length=255, null=True, blank=True)

class Veiculo(models.Model):
    modelo = models.CharField('Modelo', max_length=150)
    marca = models.CharField('Marca', max_length=20)
    ano = models.IntegerField()
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=7)

class Produto(models.Model):
    nome_produto = models.CharField('Produto', max_length=500)
    preco = models.FloatField()
    descricao = models.TextField()
    
class Servico(models.Model):
    nome_servico = models.CharField('Servico', max_length=500)
    preco = models.FloatField()
    descricao = models.TextField()


