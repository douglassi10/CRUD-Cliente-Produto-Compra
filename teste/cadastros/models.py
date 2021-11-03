from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

SEXO = [
    ('M', 'MASCULINO'),
    ('F', 'FEMININO'),
]

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True, help_text='somente numeros')
    data_nascimento = models.DateField(help_text='ex: 12/03/1998')
    celular = models.CharField(max_length=16, help_text='ex: (83) 98556-2389')
    email = models.EmailField(verbose_name='E-mail', default='')
    sexo = models.CharField(max_length=6, choices=SEXO, default='M')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome + " (" + str(self.cpf) + ")"

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome

class Compra(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    
    cliente = ForeignKey(Cliente, on_delete=models.PROTECT)
    produto = ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return 'compra de ' + self.produto.nome

