from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UsuarioCreationForm,pecasForm, Tipo_pecasForm,entrada_pecasForm
#importações dos cruds
from .models import pecas,Tipo_pecas, entrada_pecas, Venda, Venda_pecas

# Create your views here.
def home(request):
    return render(request, 'index.html',{'nome':'IFRN'})
@login_required
def perfil(request):
    return render(request, 'perfil.html')
@login_required      
def registro(request):
    form = UsuarioCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login') 
    contexto={
        'form':form
    }        
    return render(request, 'registro.html',contexto)


#CRUDS DO SISTEMA
#peças
@login_required
def lista_pecas(request):
    Pecas=pecas.objects.all()
    contexto={
        'lista_pecas': Pecas
    }
    return render(request,'pecas.html',contexto)
@login_required    
def cadastro(request):
    form= pecasForm(request.POST or None)
    if form.is_valid():
           form.save()
           return redirect('lista_pecas') 
    contexto={
        'form':form
    }   
    return render(request,'cadastro.html',contexto)

def atualizar(request, id):
    Pecas=pecas.objects.get(pk=id)
    form = pecasForm(request.POST or None, instance=Pecas)

    if form.is_valid():
        form.save()
        return redirect('lista_pecas')

    contexto = {
        'form':form
    }    
    return render(request, 'cadastro.html',contexto)  
@login_required
def deletar(request,id):
    Pecas=pecas.objects.get(pk=id)
    Pecas.delete()
    return redirect('lista_pecas')


#Crud de tipos de peças

def lista_tipos(request):
    lista=Tipo_pecas.objects.all() 
    contexto={
        'lista_tipos':lista
    }
    return render(request,'tipos.html',contexto)
@login_required
def tipos_cadastrar(request):
    form=Tipo_pecasForm(request.POST or None)
    if form.is_valid():
         form.save()
         return redirect('lista_tipos')

    contexto={
        'form': form
    }
    return render(request,'tipos_cadastrar.html',contexto)

def editar(request,id):
    tipos=Tipo_pecas.objects.get(pk=id)
    form = Tipo_pecasForm(request.POST or None, instance=tipos)
    if form.is_valid():
            form.save()
            return redirect('lista_tipos')
    contexto={
        'form':form
    }    
    return render(request,'tipos_cadastrar.html',contexto)

def remover(request,id):
    tipos=Tipo_pecas.objects.get(pk=id)
    tipos.delete()
    return redirect('lista_tipos') 

#cruds de entradas de peças

def entrada(request):
    entradas=entrada_pecas.objects.all()
    contexto={
        'lista_entrada':entradas
    }
    return render(request,'entradas.html',contexto)

def cadastrar_entradas(request):
    form=entrada_pecasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('entrada')
    contexto={
        'form':form
    }
    return render(request,'entradas_cadastrar.html',contexto)

def editar_entradas(request,id):
    entrada= entrada_pecas.objects.get(pk=id)
    form = entrada_pecasForm(request.POST or None, instance=entrada)
    if form.is_valid():
        form.save()
        return redirect('entrada')

    contexto={
        'form':form
    }    
    return render(request,'entradas_cadastrar.html',contexto)

def deletar_pecas(request,id):
    pecas_deletar= entrada_pecas.objects.get(pk=id)
    pecas_deletar.delete()
    return redirect('entrada')


def saidas(request):
    todas_pecas = pecas.objects.all()
    vendas = {}
    
    # if 'cpf_digitado' not in request.session:
    #     request.session['cpf_digitado'] = ''
    if 'produtos' not in request.session:
        request.session['produtos'] = {}
    
    #request.session['produtos'] = {'chave1':'chave2'}
    #request.session['produtos']['chave2'] = 'valor2'
    # if 'produtos' in request.session:
    #     vendas = request.session.get('produtos')
    # else:
    #     request.session['produtos'] = {'chave1':'chave2'}

    contexto = {
        'todas_pecas': todas_pecas,
        'vendas':vendas
        
    }
    return render(request,'saidas.html', contexto)  

def adicionar_produto_sessao(request):
    if request.POST:
        # peca_id = ''
        # vendas = request.session['produtos']
        # obj_peca = pecas.objects.get(pk=request.POST['peca'])
        peca_id = request.POST['peca']
        peca_obj = pecas.objects.get(pk=peca_id)

        qtd = request.POST['qtd']
        
        # request.session['cpf_digitado'] = request.POST['cpf']

        lista = request.session.get('produtos')
        lista[peca_id] = [peca_obj.nome, qtd]
        request.session['produtos'] = lista
        # request.session['produtos'] = vendas
    return redirect('saidas')


def finalizar_venda(request):
    lista = request.session.get('produtos')
    cpf_digitado = request.POST['cpf']
    
    venda_criada = Venda()
    venda_criada.cpf = cpf_digitado
    venda_criada.usuario = request.user
    venda_criada.save()

    produtos = request.session.get('produtos')
    chaves = list(produtos.keys())
    
    for chave in chaves:
        venda_peca = Venda_pecas()
        venda_peca.pecas = pecas.objects.get(pk=int(chave))
        venda_peca.venda = venda_criada
        venda_peca.desconto = 0
        venda_peca.quantidade = produtos[chave][1]
        venda_peca.save()

    request.session['produtos'] = {}
    
    return redirect('perfil')


def zerar_produtos(request):
    request.session['produtos'] = {}

    return redirect('saidas')










