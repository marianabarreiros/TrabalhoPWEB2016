from django.db import models
import datetime

# Create your models here.
class Pessoa(models.Model):
    endereco = models.CharField(max_length=50, default='', verbose_name='Endereço')
    bairro = models.CharField(max_length=50, default='', verbose_name='Bairro')
    municipio = models.CharField(max_length=50, default='',verbose_name='Município')
    cep = models.CharField(max_length=20, help_text="Nao use caracteres especiais: <em>40353111</em", default=' ', verbose_name='CEP')
    uf = models.CharField(max_length=2, default='', verbose_name='UF')
    telefone = models.CharField(max_length=20, help_text="Use o seguinte formato: <em>071999998888 ou 32220000</em>", default='', verbose_name='Telefone')
    email = models.EmailField(max_length=50, default='', verbose_name='E-mail')

    class Meta:
        abstract = True


class PessoaFisica(Pessoa):
    nome = models.CharField(max_length=50, default='', verbose_name='Nome')
    sobrenome = models.CharField(max_length=100, default='', verbose_name='Sobrenome')
    cpf = models.CharField(max_length=15, primary_key=True, help_text="Use o seguinte formato: <em>xxx.xxx.xxx-xx</em>", verbose_name='CPF')
    data_nascimento = models.DateField(help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>", default=datetime.date.today, verbose_name='Data de Nascimento')
    funcao = models.CharField(max_length=49, verbose_name='Funçao')

    def __str__(self):
        return "%s %s  " % (self.nome, self.sobrenome)
    class Meta:
        verbose_name = "Pessoa Física"
        verbose_name_plural = "Pessoas Física"

class PessoaJuridica(Pessoa):
    razao_social = models.CharField(max_length=45, verbose_name='Razão Social')
    cnpj = models.CharField(max_length=15, primary_key=True, verbose_name='CNPJ')

    def __str__(self):
        return "%s %s" % (self.razao_social, self.cnpj)

    class Meta:
        verbose_name = "Pessoa Jurídica"
        verbose_name_plural = "Pessoas Jurídica"

class ClientePessoaFisica(PessoaFisica):

    def __str__(self):
        return "%s %s " % (self.nome, self.sobrenome)

    class Meta:
        verbose_name = "Cliente Pessoa Física"
        verbose_name_plural = "Clientes Pessoa Física"


class ClientePessoaJuridica(PessoaJuridica):

    def __str__(self):
        return "%s %s " % (self.razao_social, self.cnpj)

    class Meta:
        verbose_name = "Cliente Pessoa Jurídica"
        verbose_name_plural = "Clientes Pessoa Jurídica"

class Empresa(PessoaJuridica):
    responsavel = models.ForeignKey(PessoaFisica, related_name='+', verbose_name='Responsável')
    inscricao_estadual = models.CharField(max_length=20, verbose_name='Inscrição Estadual')
    inscricao_municipal = models.CharField(max_length=20, verbose_name='Inscrição Municipal')

    def __str__(self):
        return "%s %s " % (self.razao_social, self.cnpj)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

class FornecedorPessoaFisica(PessoaFisica):
    cliente = models.ForeignKey(PessoaFisica, related_name='+', verbose_name='Cliente')

    def __str__(self):
        return "%s %s " % (self.nome, self.sobrenome)

    class Meta:
        verbose_name = "Fornecedor Físico"
        verbose_name_plural = "Fornecedores Físicos"

class FornecedorPessoaJuridica(PessoaJuridica):
    cliente = models.ForeignKey(PessoaJuridica, related_name='+', verbose_name='Cliente')

    def __str__(self):
        return "%s %s " % (self.razao_social, self.cnpj)

    class Meta:
        verbose_name = "Fornecedor Júridico"
        verbose_name_plural = "Fornecedores Júridicos"

class LancamentosReceber(models.Model):
    id_lancamentos_receber = models.PositiveIntegerField(primary_key=True, verbose_name='Identificação do Lançamento a Receber')
    cliente = models.ForeignKey(ClientePessoaJuridica, ClientePessoaFisica, related_name="+", verbose_name='Cliente')
    empresa = models.ForeignKey(Empresa, related_name="+", verbose_name='Empresa')
    data_vencimento = models.DateField(default=datetime.date.today, verbose_name='Data de Vencimento')
    data_emissao = models.DateField(default=datetime.date.today, help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>", verbose_name='Data de Emissão')
    valor_titulo = models.FloatField(help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>", verbose_name='Valor do Título')
    numero_documento = models.CharField(max_length=20, verbose_name='Número do Documento')

    def __str__(self):
        return "%s %s %s %s %s %s %s " % (self.identificador, self.cliente, self.empresa, self.data_vencimento, self.data_emissao, self.valor_titulo, self.numero_documento)

    class Meta:
        verbose_name = "Laçamento a Receber"
        verbose_name_plural = "Laçamentos a Receber"

class LancamentosPagar(models.Model):
    id_lancamentos_pagar = models.PositiveIntegerField(primary_key=True, verbose_name='Identificação do Lançamento a Pagar')
    fornecedor = models.ForeignKey(FornecedorPessoaFisica, FornecedorPessoaJuridica, related_name="+", verbose_name='Fornecedor')
    empresa = models.ForeignKey(Empresa, related_name="+", verbose_name='Empresa')
    data_vencimento = models.DateField(default=datetime.date.today, verbose_name='Data de Vencimento')
    data_emissao = models.DateField(default=datetime.date.today, help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>", verbose_name='Data de Emissão')
    valor_titulo = models.FloatField(default=0, verbose_name='Valor do Título')
    numero_documento = models.CharField(max_length=20, verbose_name='Número de Documento')

    def __str__(self):
        return "%s %s %s %s %s %s %s " % (self.identificador, self.fornecedor, self.empresa, self.data_vencimento, self.data_emissao, self.valor_titulo, self.numero_documento)

    class Meta:
        verbose_name = "Laçamento a Pagar"
        verbose_name_plural = "Laçamentos a Pagar"

class FormasPagamentos(models.Model):
    id_forma_pagamento = models.CharField(max_length= 10, primary_key=True, verbose_name='Forma de Pagamento')
    descricao = models.CharField(max_length= 20, verbose_name='Descrição')

    def __str__(self):
        return "%s %s " % (self.idenid_forma_pagamento, self.descricao)

    class Meta:
        verbose_name = "Forma de Pagamento"
        verbose_name_plural = "Formas de Pagamento"

class BaixasReceber(models.Model):
    id_baixa_receber = models.CharField(max_length  = 10, primary_key=True, verbose_name='Identificação')
    id_forma_pagamento = models.ForeignKey(FormasPagamentos, related_name="+", verbose_name='Forma de Pagamento')
    id_lancamentos_receber = models.ForeignKey(LancamentosReceber, related_name="+", verbose_name='Identificação Lançamento a Receber')
    banco = models.CharField(max_length  = 20, verbose_name='Banco')
    disponibilidade = models.CharField(max_length = 20, verbose_name='Disponibilidade')
    data_baixa = models.DateField(help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>", verbose_name='Data de Baixa')
    valor_pago = models.FloatField(default='0', verbose_name='Valor Pago')
    residual = models.CharField(max_length = 20, verbose_name='Residual')

    def __str__(self):
        return "%s %s %s %s %s %s %s %s  " % (self.id_baixa_receber, self.id_forma_pagamento, self.id_lancamentos_receber, self.banco, self.disponibilidade, self.data_baixa, self.valor_pago, self.residual)

    class Meta:
        verbose_name = "Baixa a Receber"
        verbose_name_plural = "Baixas a Receber"

class BaixasPagar(models.Model):
    id_baixa_pagar = models.CharField(max_length  = 10, primary_key=True, verbose_name='Identificação')
    id_forma_pagamento = models.ForeignKey(FormasPagamentos, related_name="+", verbose_name='Forma de Pagamento')
    id_lancamentos_pagar = models.ForeignKey(LancamentosPagar, related_name="+", verbose_name='Identificaçao do Pagamento a Pagar')
    banco = models.CharField(max_length  = 20, verbose_name='Banco')
    disponibilidade = models.CharField(max_length  = 20, verbose_name='Disponibilidade')
    data_baixa = models.DateField(help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>", verbose_name='Data da Baixa')
    valor_pago = models.FloatField(default= 0, verbose_name='Valo Pago')
    residual = models.CharField(max_length  = 20, verbose_name='Residual')

    def __str__(self):
        return "%s %s %s %s %s %s %s %s  " % (self.id_baixa_pagar, self.id_forma_pagamento, self.id_lancamentos_pagar, self.banco, self.disponibilidade, self.data_baixa, self.valor_pago, self.residual)

    class Meta:
        verbose_name = "Baixa a Pagar"
        verbose_name_plural = "Baixas a Pagar"

class ContasBancarias(models.Model):
    id_contas_bancarias = models.IntegerField(primary_key = True, verbose_name='Identificação')
    classificacao = models.CharField(max_length  = 20, verbose_name='Classificação')
    descricao = models.CharField(max_length=20, verbose_name='Descrição')
    numero_conta = models.CharField(max_length = 20, verbose_name='Número da Conta')
    numero_agencia = models.CharField(max_length = 20, verbose_name='Núemro da Agência')
    data_saldo_inicial = models.DateField(help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>", verbose_name='Data do Saldo Inicial')
    saldo_inicial = models.FloatField(default=0, verbose_name='Saldo Inicial')
    caixa = models.CharField(max_length = 20, verbose_name='Caixa')
    banco = models.CharField(max_length = 20, verbose_name='Banco')

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s   " % (self.id_contas_bancarias, self.classificacao, self.descricao, self.numero_conta, self.numero_agencia, self.data_saldo_inicial, self.saldo_inicial, self.caixa, self.banco)

    class Meta:
        verbose_name = "Conta Bancária"
        verbose_name_plural = "Contas Bancária"


class PlanoDeContas(models.Model):
    id_plano_contas = models.PositiveIntegerField(primary_key=True, verbose_name='Identificação')
    contas_bancarias = models.ForeignKey(ContasBancarias, related_name="+", verbose_name='Contas Bancárias')
    classificacao = models.CharField(max_length  = 20, verbose_name='Classificação')
    tipo_conta = models.CharField(max_length  = 20, verbose_name='Tipo da conta')
    descricao = models.CharField(max_length  = 20, verbose_name='Descrição')
    caixa = models.CharField(max_length  = 20, verbose_name='Caixa')
    banco = models.CharField(max_length  = 20, verbose_name='Banco')
    cliente = models.CharField(max_length  = 20, verbose_name='Cliente')
    fornecedor = models.CharField(max_length  = 20, verbose_name='Fornecedeor')
    entrada_recurso = models.CharField(max_length  = 20, verbose_name='Entrada do Recurso')
    saida_recurso = models.CharField(max_length  = 20, verbose_name='Saída do Recurso')

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s   " % (self.id_plano_contas, self.contas_bancarias, self.classificacao, self.tipo_conta, self.descricao, self.caixa, self.banco, self.cliente, self.fornecedor, self.entrada_recurso, self.saida_recurso)

    class Meta:
        verbose_name = "Baixa a Receber"
        verbose_name_plural = "Baixas a Receber"

class Tesouraria(models.Model):
    empresa = models.ForeignKey(Empresa, related_name="+", verbose_name='Empresa')
    cliente = models.ForeignKey(ClientePessoaJuridica, related_name="+", verbose_name='Cliente')
    fornecedor = models.ForeignKey(FornecedorPessoaJuridica, related_name="+", verbose_name='Fornecedor')
    conta_entrada = models.ForeignKey(ContasBancarias, related_name="+", verbose_name='Conta de Entrada')
    conta_saida = models.ForeignKey(ContasBancarias, related_name="+", verbose_name='Conta de Saída')
    valor = models.FloatField(default=0, verbose_name='Valor')
    numero_documento = models.IntegerField(default=0, verbose_name='Númedo do Documnto')
    data_emissao = models.DateField(default=datetime.date.today, verbose_name='Data de Emissão')
    data_vencimento = models.DateField(default=datetime.date.today, verbose_name='Data de Vencimento')
    data_disponibilidade = models.DateField(default=datetime.date.today, verbose_name='Data de Disponibilidade')

    class Meta:
        verbose_name = "Tesouraria"
        verbose_name_plural = "Tesourarias"


