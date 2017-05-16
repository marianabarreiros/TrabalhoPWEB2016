from django.http import HttpResponse
from django.shortcuts import render
from .models import PessoaFisica
from .models import PessoaJuridica
from .models import FornecedorPessoaFisica
from .models import FornecedorPessoaJuridica
from .models import ClientePessoaFisica
from .models import ClientePessoaJuridica
from .models import Empresa
from .models import LancamentosPagar
from .models import LancamentosReceber
from .models import PlanoDeContas
from .models import Tesouraria
from .models import BaixasPagar
from .models import BaixasReceber
from .forms import LancamentoReceberForm
from django.shortcuts import redirect

#this_path = os.getcwd() + '/financeiro/'
# Create your views here.
def tela_inicial(request):
    return render(request, 'financeiro/tela_inicial.html', {})

def tela_cadastro_cliente_fisico(request):
    return render(request, 'financeiro/tela_cadastro_cliente_fisico.html', {})

def tela_cadastro_cliente_juridico(request):
    return render(request, 'financeiro/tela_cadastro_cliente_juridico.html', {})

def tela_cadastro_empresa(request):
    return render(request, 'financeiro/tela_cadastro_empresa.html', {})

def tela_fornecedor_juridico(request):
    return render(request, 'financeiro/tela_fornecedor_juridico.html', {})

def tela_fornecedor_fisico(request):
    return render(request, 'financeiro/tela_fornecedor_fisico.html', {})

def tela_plano_de_conta(request):
    return render(request, 'financeiro/tela_plano_de_conta.html', {})

def tela_formas_de_pagamento(request):
    return render(request, 'financeiro/tela_cadastro_formas_de_pagamento.html', {})

def tela_conta_bancaria(request):
    return render(request, 'financeiro/tela_cadastro_conta_bancaria.html', {})

def tela_baixas_pagar(request):
    return render(request, 'financeiro/tela_cadastro_baixas_pagar.html', {})

def tela_baixas_receber(request):
    return render(request, 'financeiro/tela_cadastro_baixas_receber.html', {})

def tela_lancamentos_pagar(request):
    return render(request, 'financeiro/tela_cadastro_lancamentos_pagar.html', {})

def tela_lancamentos_receber(request):
    form = LancamentoReceberForm()
    return render(request, 'financeiro/tela_cadastro_lancamentos_receber.html', {'form': form})

def lancamentos_receber(request):
    #form = LancamentoReceberForm()
    #return render(request, 'financeiro/Tela_cadastro_lancamentos_receber.html', {'form': form})
    if request.method == "POST":
            form = LancamentoReceberForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.salvar()
            else:
                form = LancamentoReceberForm()
            return render(request, 'financeiro/lancamentos_receber.html', {'form': form})


def tela_tesouraria(request):
    return render(request, 'financeiro/tela_cadastro_tesouraria.html', {})

#Funções para as telas referentes a Opçao "Relatórios" do Menu

def tela_recupera_contas_receber(request):
    receber = LancamentosReceber.objects.all().order_by('empresa')
    return render(request, 'financeiro/tela_recupera_contas_receber.html', {'receber' : receber})

def tela_recupera_contas_pagar(request):
    pagar = LancamentosPagar.objects.all().order_by('empresa')
    return render(request, 'financeiro/tela_recupera_contas_pagar.html', {'pagar' : pagar})

def tela_recupera_movimentos(request):
    tesouraria = Tesouraria.objects.all().order_by('empresa')
    return render(request, 'financeiro/tela_recupera_movimentos.html', {'tesouraria' : tesouraria})

def tela_recupera_fluxo_caixa(request):
    fluxo = Tesouraria.objects.all().order_by('empresa')
    return render(request, 'financeiro/tela_recupera_fluxo_caixa.html', {'fluxo' : fluxo})
