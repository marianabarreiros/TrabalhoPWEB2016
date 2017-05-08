from django.shortcuts import render

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
    return render(request, 'financeiro/tela_cadastro_lancamentos_receber.html', {})

def tela_tesouraria(request):
    return render(request, 'financeiro/tela_cadastro_tesouraria.html', {})

