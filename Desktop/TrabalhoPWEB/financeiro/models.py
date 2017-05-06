from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    cep = models.CharField(max_length=20, help_text="Nao use caracteres especiais: <em>40353111</em")
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20, help_text="Use o seguinte formato: <em>071999998888 ou 32220000</em>")
    email = models.EmailField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s" % (self.nome, self.sobrenome, self.endereco, self.bairro, self.municipio, self.cep, self.uf, self.telefone, self.email)

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=15, primary_key=True, help_text="Use o seguinte formato: <em>xxx.xxx.xxx-xx</em>")
    data_nascimento = models.DateField(help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>")
    funcao = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s %s " % (self.cpf, self.data_nascimento, self.funcao)

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=15, primary_key=True)
    razao_social = models.CharField(max_length=45)

    def __str__(self):
        return "%s %s" % (self.cnpj, self.razao_social)

class ClientePessoaFisica(PessoaFisica):
    cpf_do_vendedor = models.ForeignKey(PessoaFisica, related_name='+')

    def __str__(self):
        return "%s " % (self.cpf_do_vendedor)

class ClientePessoaJuridica(PessoaJuridica):
    cnpj_do_vendedor = models.ForeignKey(PessoaJuridica, related_name='+')

    def __str__(self):
        return "%s " % (self.cnpj_do_vendedor)


class Empresa(PessoaJuridica):
    responsavel = models.ForeignKey(PessoaFisica, related_name='+')
    inscricao_estadual = models.CharField(max_length=20)
    inscricao_municipal = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s %s" % (self.responsavel, self.inscricao_municipal, self.inscricao_estadual)

class FornecedorPessoaFisica(PessoaFisica):
    cliente = models.ForeignKey(PessoaFisica, related_name='+')

    def __str__(self):
        return "%s " % (self.cliente)

class FornecedorPessoaJuridica(PessoaJuridica):
    cliente = models.ForeignKey(PessoaJuridica, related_name='+')

    def __str__(self):
        return "%s " % (self.cliente)


class LancamentosReceber(models.Model):
    id_lancamentos_receber = models.PositiveIntegerField(primary_key=True)
    cliente = models.ForeignKey(ClientePessoaJuridica, ClientePessoaFisica, related_name="+")
    empresa = models.ForeignKey(Empresa, related_name="+")
    data_vencimento = models.DateField
    data_emissao = models.DateField(help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>")
    valor_titulo = models.FloatField(help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>")
    numero_documento = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s %s %s %s %s %s " % (self.identificador, self.cliente, self.empresa, self.data_vencimento, self.data_emissao, self.valor_titulo, self.numero_documento)


class LancamentosPagar(models.Model):
    id_lancamentos_pagar = models.PositiveIntegerField(primary_key=True)
    fornecedor = models.ForeignKey(FornecedorPessoaFisica, FornecedorPessoaJuridica, related_name="+")
    empresa = models.ForeignKey(Empresa, related_name="+")
    data_vencimento = models.DateField
    data_emissao = models.DateField(help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>")
    valor_titulo = models.FloatField
    numero_documento = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s %s %s %s %s %s " % (self.identificador, self.fornecedor, self.empresa, self.data_vencimento, self.data_emissao, self.valor_titulo, self.numero_documento)

class FormasPagamentos(models.Model):
    id_forma_pagamento = models.CharField(max_length= 10, primary_key=True)
    descricao = models.CharField(max_length= 20)

    def __str__(self):
        return "%s %s " % (self.idenid_forma_pagamento, self.descricao)

class BaixasReceber(models.Model):
    id_baixa_receber = models.CharField(max_length  = 10, primary_key=True)
    id_forma_pagamento = models.ForeignKey(FormasPagamentos, related_name="+")
    id_lancamentos_receber = models.ForeignKey(LancamentosReceber, related_name="+")
    banco = models.CharField(max_length  = 20)
    disponibilidade = models.CharField(max_length = 20)
    data_baixa = models.DateField(help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>")
    valor_pago = models.FloatField
    residual = models.CharField(max_length = 20)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s  " % (self.id_baixa_receber, self.id_forma_pagamento, self.id_lancamentos_receber, self.banco, self.disponibilidade, self.data_baixa, self.valor_pago, self.residual)


class BaixasPagar(models.Model):
    id_baixa_pagar = models.CharField(max_length  = 10, primary_key=True)
    id_forma_pagamento = models.ForeignKey(FormasPagamentos, related_name="+")
    id_lancamentos_pagar = models.ForeignKey(LancamentosPagar, related_name="+")
    banco = models.CharField(max_length  = 20)
    disponibilidade = models.CharField(max_length  = 20)
    data_baixa = models.DateField(help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>")
    valor_pago = models.FloatField
    residual = models.CharField(max_length  = 20)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s  " % (self.id_baixa_pagar, self.id_forma_pagamento, self.id_lancamentos_pagar, self.banco, self.disponibilidade, self.data_baixa, self.valor_pago, self.residual)

class ContasBancarias(models.Model):
    id_contas_bancarias = models.IntegerField(primary_key = True)
    classificacao = models.CharField(max_length  = 20)
    descricao = models.CharField(max_length=20)
    numero_conta = models.CharField(max_length = 20)
    numero_agencia = models.CharField(max_length = 20)
    data_saldo_inicial = models.DateField(help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>")
    saldo_inicial = models.FloatField
    caixa = models.CharField(max_length = 20)
    banco = models.CharField(max_length = 20)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s   " % (self.id_contas_bancarias, self.classificacao, self.descricao, self.numero_conta, self.numero_agencia, self.data_saldo_inicial, self.saldo_inicial, self.caixa, self.banco)


class PlanoDeContas(models.Model):
    id_plano_contas = models.PositiveIntegerField(primary_key=True)
    contas_bancarias = models.ForeignKey(ContasBancarias, related_name="+")
    classificacao = models.CharField(max_length  = 20)
    tipo_conta = models.CharField(max_length  = 20)
    descricao = models.CharField(max_length  = 20)
    caixa = models.CharField(max_length  = 20)
    banco = models.CharField(max_length  = 20)
    cliente = models.CharField(max_length  = 20)
    fornecedor = models.CharField(max_length  = 20)
    entrada_recurso = models.CharField(max_length  = 20)
    saida_recurso = models.CharField(max_length  = 20)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s   " % (self.id_plano_contas, self.contas_bancarias, self.classificacao, self.tipo_conta, self.descricao, self.caixa, self.banco, self.cliente, self.fornecedor, self.entrada_recurso, self.saida_recurso)

class Tesouraria(models.Model):
    empresa = models.ForeignKey(Empresa, related_name="+")
    cliente = models.ForeignKey(ClientePessoaJuridica, related_name="+")
    fornecedor = models.ForeignKey(FornecedorPessoaJuridica, related_name="+")
    conta_entrada = models.ForeignKey(ContasBancarias, related_name="+")
    conta_saida = models.ForeignKey(ContasBancarias, related_name="+")
    valor = models.FloatField
    numero_documento = models.IntegerField
    data_emissao = models.DateField
    data_vencimento = models.DateField
    data_disponibilidade = models.DateField


