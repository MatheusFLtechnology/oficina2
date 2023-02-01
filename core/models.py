from django.db import models

from django.contrib.auth.models import AbstractUser

#Banco de dados do Sistema

#tabela de perfil
class Perfil(models.Model):
    nome = models.CharField('Nome', max_length=50)
#tabela de usuario
class Usuario(AbstractUser):
   cpf = models.CharField('cpf', max_length=11, unique=True)
   nome = models.CharField('nome', max_length=100)
   idade = models.IntegerField('idade')
   perfil= models.ManyToManyField(Perfil)
#tabela de fornecedor
class fornecedor(models.Model):
   Nome=models.CharField('Nome',max_length=50)
   cnpj=models.IntegerField('Cnpj')

#tabela de tipos de peças
class Tipo_pecas(models.Model):
   nome=models.CharField('Nome', max_length=100)
   marca=models.CharField('Nome',max_length=50)

   def __str__(self):
        return self.nome

#tabela de vendas
class Venda(models.Model):
   data_da_venda=models.DateField('Data de cadastro',null=True)
   usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
   cpf = models.CharField('CPF', max_length=11)
   
      
#tabela de peças
class pecas(models.Model):
   nome=models.CharField('Nome',max_length=100)
   data_cadastro=models.DateField('Data de cadastro',null=True, auto_now_add=False)
   descricao= models.CharField('Descrição', max_length=40)
   marca=models.CharField('Marca',max_length=100)
   fornecedor=models.CharField('Fornecedor',max_length=50)
   Tipo_pecas = models.ForeignKey(Tipo_pecas, on_delete=models.PROTECT)  
   valor_venda = models.FloatField('Valor de venda')

   def __str__(self):
      return self.nome
#tabela de vendas de peças
class Venda_pecas(models.Model):
   pecas=models.ForeignKey(pecas,on_delete=models.PROTECT)
   venda=models.ForeignKey(Venda,on_delete=models.PROTECT)
   desconto=models.IntegerField('desconto')
   quantidade=models.IntegerField('quantidade')


#tabela de entradas de peças   
class entrada_pecas(models.Model):
   pecas=models.ForeignKey(pecas,on_delete=models.PROTECT)  
   quantidade=models.IntegerField('quantidade')
   data=models.DateField('Data de cadastro',null=True, auto_now_add=False) 
   valor_compra=models.DecimalField('valor da compra',max_digits=10,decimal_places=2)

   
   


   

   





    


