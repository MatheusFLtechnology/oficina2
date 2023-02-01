"""oficina_02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home,perfil, registro,lista_pecas,cadastro,atualizar,deletar,lista_tipos,tipos_cadastrar,editar,remover,entrada,cadastrar_entradas,editar_entradas,deletar_pecas
from core.views import saidas, adicionar_produto_sessao, zerar_produtos, finalizar_venda
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('perfil/', perfil, name='perfil'),
    path('registro/', registro, name='registro'),
    path('lista_pecas/', lista_pecas, name='lista_pecas'),
    path('cadastro/', cadastro, name='cadastro'),
    path('atualizar/<int:id>/', atualizar, name='atualizar'),
    path('deletar/<int:id>/', deletar, name='deletar'),

#tipos de peças
    path('lista_tipos/', lista_tipos, name='lista_tipos'),
    path('tipos_cadastrar/', tipos_cadastrar, name='tipos_cadastrar'),
    path('editar/<int:id>/',editar, name='editar'),
    path('remover/<int:id>/',remover, name='remover'),
    path('', home, name='home'),
    path('admin/', admin.site.urls),

#entradadas de peças
    path('entrada/',entrada, name='entrada'),
    path('cadastrar_entradas/', cadastrar_entradas, name='cadastrar_entradas'),  
    path('editar_entradas/<int:id>/',editar_entradas, name='editar_entradas'), 
    path('deletar_pecas/<int:id>/',deletar_pecas, name='deletar_pecas'), 

    path('saidas/',saidas, name='saidas'),
    path('adicionar_produto_sessao/',adicionar_produto_sessao,name='adicionar_produto_sessao'),
    path('zerar_produtos/',zerar_produtos, name='zerar_produtos'),
    path('finalizar_venda/',finalizar_venda, name='finalizar_venda'),

]
