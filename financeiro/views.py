import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
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

this_path = os.getcwd() + '/financeiro/'
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

#Funções para as telas referentes a Opçao "Relatórios" do Menu
'''
def index(request):
    return HttpResponse("Hello, world")'''

def tela_recupera_contas_receber(request):
    '''
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="contasreceber.pdf"'

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    #Cabeçalho
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30,750,'Sistema Financeiro')

    c.setFont('Helvetica', 12)
    c.drawString(30,735,'Contas a Receber')

    c.setFont('Helvetica-Bold', 12)
    c.drawString(480,750,'16/05/2016')
    c.line(460,747,560,747)

    #Cabeçalho da Tabela
    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontSize = 10

   id = Paragraph('''''', styleBH)
    clientef = Paragraph('''''', styleBH)
    clientej = Paragraph('''''', styleBH)
    empresa = Paragraph('''''', styleBH)
    venc = Paragraph('''''', styleBH)
    emissao = Paragraph('''''', styleBH)
    valor = Paragraph('''''', styleBH)
    documento = Paragraph(''''' '''

    data = []
    data.append([id, clientef, clientej, empresa, venc, emissao, valor, documento])

    #Tabela
    styleN = styles["BodyText"]
    styleN.alignment = TA_CENTER
    styleN.fontSize = 7

    high = 650
    for

    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
    #----------'''
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
