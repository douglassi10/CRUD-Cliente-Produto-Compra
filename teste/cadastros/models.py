from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=16)

    def __str__(self):
        return self.nome + " (" + str(self.cpf) + ")"

class Produto(models.Model):
    nome = models.CharField(max_length=20)
    preco = models.FloatField()

    def __str__(self):
        return self.nome

class Compra(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    
    cliente = ForeignKey(Cliente, on_delete=models.PROTECT)
    produto = ForeignKey(Produto, on_delete=models.PROTECT)

