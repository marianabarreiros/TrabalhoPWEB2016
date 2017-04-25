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
 
class LancamentosReceber(ClientePessoaFisica, ClientePessoaJuridica, Empresa):
    identificador = models.PositiveIntegerField(primary_key=True)
    cliente = models.ForeignKey(ClientePessoaJuridica, ClientePessoaFisica, related_name="+")
    empresa = models.ForeignKey(Empresa, related_name="+")
    data_vencimento = models.DateField
    data_emissao = models.dateField(help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>")
    valor_titulo = models.FloatField(help_text="Use o seguinte formato: <em>DD/MM/AAAA</em>")
    numero_documento = models.CharFiedl(max_length=20)
    
    def __str__(self):
        return "%s %s %s %s %s %s %s " % (self.identificador, self.cliente, self.empresa, self.data_vencimento, self.data_emissao, self.valor_titulo, self.numero_documento)
