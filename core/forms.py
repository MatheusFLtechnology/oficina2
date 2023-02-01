from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario,pecas,Tipo_pecas,entrada_pecas




class UsuarioCreationForm(UserCreationForm):
    class Meta:
       model = Usuario
       fields= ['username', 'password1','password2','cpf','email','nome','idade']

class pecasForm(ModelForm):
    class Meta:
        model= pecas
        fields=['nome','descricao','Tipo_pecas','marca','fornecedor','valor_venda']   

class Tipo_pecasForm(ModelForm):
    class Meta:
        model= Tipo_pecas
        fields=['nome','marca']            

class entrada_pecasForm(ModelForm):
    class Meta:
        model=entrada_pecas
        fields=["pecas","quantidade","valor_compra"]        