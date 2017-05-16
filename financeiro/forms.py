from django import forms
from .models import PessoaFisica
from .models import ClientePessoaFisica
from .models import PessoaJuridica
from .models import ClientePessoaJuridica
from .models import Empresa
from .models import FornecedorPessoaFisica
from .models import FornecedorPessoaJuridica
from .models import LancamentosPagar
from .models import LancamentosReceber
from .models import FormasPagamentos
from .models import BaixasReceber
from .models import BaixasPagar
from .models import ContasBancarias
from .models import PlanoDeContas
from .models import Tesouraria

class PessoaFisicaForm(forms.ModelForm):
    class Meta():
        model = PessoaFisica
        fields = ['nome', 'sobrenome', 'cpf', 'data_nascimento', 'funcao', 'endereco', 'bairro', 'municipio', 'cep', 'uf', 'telefone', 'email']

class PessoaJuridicaForm(forms.ModelForm):
    class Meta():
        model = PessoaJuridica
        fields = ['razao_social', 'cnpj', 'endereco', 'bairro', 'municipio', 'cep', 'uf', 'telefone', 'email']

class ClientePessoaFisicaForm(forms.ModelForm):
    class Meta():
        model = ClientePessoaFisica
        fields = ['nome', 'sobrenome', 'cpf', 'data_nascimento', 'funcao', 'endereco', 'bairro', 'municipio', 'cep', 'uf', 'telefone', 'email']

class ClientePessoaJuridicaForm(forms.ModelForm):
    class Meta():
        model = ClientePessoaJuridica
        fields = ['razao_social', 'cnpj', 'endereco', 'bairro', 'municipio', 'cep', 'uf', 'telefone', 'email']

class EmpresaForm(forms.ModelForm):
    class Meta():
        model = Empresa
        fields = ['razao_social', 'cnpj', 'endereco', 'bairro', 'municipio', 'cep', 'uf', 'telefone', 'email']

class FornecedorPessoaFisicaForm(forms.ModelForm):
    class Meta():
        model = FornecedorPessoaFisica
        fields = ['nome', 'sobrenome', 'cpf', 'data_nascimento', 'funcao', 'endereco', 'bairro', 'municipio', 'cep', 'uf', 'telefone', 'email']

class FornecedorPessoaJuridicaForm(forms.ModelForm):
    class Meta():
        model = FornecedorPessoaJuridica
        fields = ['razao_social', 'cnpj', 'endereco', 'bairro', 'municipio', 'cep', 'uf', 'telefone', 'email']

class LancamentoReceberForm(forms.ModelForm):
    class Meta:
        model = LancamentosReceber
        fields = ['id_lancamentos_receber', 'clienteFisico', 'clienteJuridico', 'empresa', 'data_vencimento', 'data_emissao', 'valor_titulo', 'numero_documento']

class LancamentoPagarForm(forms.ModelForm):
    class Meta:
        model = LancamentosPagar
        fields = ['id_lancamentos_pagar', 'fornecedorFisico', 'fornecedorJuridico', 'empresa', 'data_vencimento', 'data_emissao', 'valor_titulo', 'numero_documento']

class FormasPagamentosForm(forms.ModelForm):
    class Meta:
        model = FormasPagamentos
        fields = ['id_forma_pagamento', 'descricao']


class BaixasRecebersForm(forms.ModelForm):
    class Meta:
        model = BaixasReceber
        fields = ['id_baixa_receber', 'id_forma_pagamento', 'id_lancamentos_receber', 'banco', 'disponibilidade', 'data_baixa', 'valor_pago','residual']

class BaixasPagarForm(forms.ModelForm):
    class Meta:
        model = BaixasPagar
        fields = ['id_baixa_pagar', 'id_forma_pagamento', 'id_lancamentos_pagar', 'banco', 'disponibilidade', 'data_baixa', 'valor_pago','residual']

class ContasBancariasForm(forms.ModelForm):
    class Meta:
        model = ContasBancarias
        fields = ['id_contas_bancarias', 'classificacao', 'descricao',  'numero_conta', 'numero_agencia',  'data_saldo_inicial', 'saldo_inicial',   'caixa', 'banco']

class PlanoDeContasForm(forms.ModelForm):
    class Meta:
        model = PlanoDeContas
        fields = ['id_plano_contas', 'contas_bancarias', 'classificacao',  'tipo_conta', 'descricao', 'caixa', 'banco', 'cliente', 'fornecedor', 'entrada_recurso', 'saida_recurso']

class TesourariaForm(forms.ModelForm):
    class Meta:
        model = Tesouraria
        fields = ['empresa', 'cliente',    'fornecedor', 'conta_entrada', 'conta_saida', 'valor', 'numero_documento', 'data_emissao', 'data_vencimento', 'data_disponibilidade']