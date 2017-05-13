# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 13:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import financeiro.models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baixaspagar',
            name='valor_pago',
            field=models.FloatField(default=0, verbose_name='Valo Pago'),
        ),
        migrations.AddField(
            model_name='baixasreceber',
            name='valor_pago',
            field=models.FloatField(default='0', verbose_name='Valor Pago'),
        ),
        migrations.AddField(
            model_name='contasbancarias',
            name='saldo_inicial',
            field=models.FloatField(default=0, verbose_name='Saldo Inicial'),
        ),
        migrations.AddField(
            model_name='lancamentospagar',
            name='data_vencimento',
            field=models.DateField(default=datetime.date.today, verbose_name='Data de Vencimento'),
        ),
        migrations.AddField(
            model_name='lancamentospagar',
            name='valor_titulo',
            field=models.FloatField(default=0, verbose_name='Valor do Título'),
        ),
        migrations.AddField(
            model_name='lancamentosreceber',
            name='data_vencimento',
            field=models.DateField(default=datetime.date.today, verbose_name='Data de Vencimento'),
        ),
        migrations.AddField(
            model_name='tesouraria',
            name='data_disponibilidade',
            field=models.DateField(default=datetime.date.today, verbose_name='Data de Disponibilidade'),
        ),
        migrations.AddField(
            model_name='tesouraria',
            name='data_emissao',
            field=models.DateField(default=datetime.date.today, verbose_name='Data de Emissão'),
        ),
        migrations.AddField(
            model_name='tesouraria',
            name='data_vencimento',
            field=models.DateField(default=datetime.date.today, verbose_name='Data de Vencimento'),
        ),
        migrations.AddField(
            model_name='tesouraria',
            name='numero_documento',
            field=models.IntegerField(default=0, verbose_name='Númedo do Documnto'),
        ),
        migrations.AddField(
            model_name='tesouraria',
            name='valor',
            field=models.FloatField(default=0, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='baixaspagar',
            name='banco',
            field=models.CharField(max_length=20, verbose_name='Banco'),
        ),
        migrations.AlterField(
            model_name='baixaspagar',
            name='data_baixa',
            field=models.DateField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>', verbose_name='Data da Baixa'),
        ),
        migrations.AlterField(
            model_name='baixaspagar',
            name='disponibilidade',
            field=models.CharField(max_length=20, verbose_name='Disponibilidade'),
        ),
        migrations.AlterField(
            model_name='baixaspagar',
            name='id_baixa_pagar',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Identificação'),
        ),
        migrations.AlterField(
            model_name='baixaspagar',
            name='id_forma_pagamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.FormasPagamentos', verbose_name='Forma de Pagamento'),
        ),
        migrations.AlterField(
            model_name='baixaspagar',
            name='id_lancamentos_pagar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.LancamentosPagar', verbose_name='Identificaçao do Pagamento a Pagar'),
        ),
        migrations.AlterField(
            model_name='baixaspagar',
            name='residual',
            field=models.CharField(max_length=20, verbose_name='Residual'),
        ),
        migrations.AlterField(
            model_name='baixasreceber',
            name='banco',
            field=models.CharField(max_length=20, verbose_name='Banco'),
        ),
        migrations.AlterField(
            model_name='baixasreceber',
            name='data_baixa',
            field=models.DateField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>', verbose_name='Data de Baixa'),
        ),
        migrations.AlterField(
            model_name='baixasreceber',
            name='disponibilidade',
            field=models.CharField(max_length=20, verbose_name='Disponibilidade'),
        ),
        migrations.AlterField(
            model_name='baixasreceber',
            name='id_baixa_receber',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Identificação'),
        ),
        migrations.AlterField(
            model_name='baixasreceber',
            name='id_forma_pagamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.FormasPagamentos', verbose_name='Forma de Pagamento'),
        ),
        migrations.AlterField(
            model_name='baixasreceber',
            name='id_lancamentos_receber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.LancamentosReceber', verbose_name='Identificação Lançamento a Receber'),
        ),
        migrations.AlterField(
            model_name='baixasreceber',
            name='residual',
            field=models.CharField(max_length=20, verbose_name='Residual'),
        ),
        migrations.AlterField(
            model_name='clientepessoafisica',
            name='cpf_do_vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.PessoaFisica', verbose_name='CPF do Vendedor'),
        ),
        migrations.AlterField(
            model_name='clientepessoajuridica',
            name='cnpj_do_vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.PessoaJuridica', verbose_name='CNPJ do Vendedor'),
        ),
        migrations.AlterField(
            model_name='contasbancarias',
            name='banco',
            field=models.CharField(max_length=20, verbose_name='Banco'),
        ),
        migrations.AlterField(
            model_name='contasbancarias',
            name='caixa',
            field=models.CharField(max_length=20, verbose_name='Caixa'),
        ),
        migrations.AlterField(
            model_name='contasbancarias',
            name='classificacao',
            field=models.CharField(max_length=20, verbose_name='Classificação'),
        ),
        migrations.AlterField(
            model_name='contasbancarias',
            name='data_saldo_inicial',
            field=models.DateField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>', verbose_name='Data do Saldo Inicial'),
        ),
        migrations.AlterField(
            model_name='contasbancarias',
            name='descricao',
            field=models.CharField(max_length=20, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='contasbancarias',
            name='id_contas_bancarias',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Identificação'),
        ),
        migrations.AlterField(
            model_name='contasbancarias',
            name='numero_agencia',
            field=models.CharField(max_length=20, verbose_name='Núemro da Agência'),
        ),
        migrations.AlterField(
            model_name='contasbancarias',
            name='numero_conta',
            field=models.CharField(max_length=20, verbose_name='Número da Conta'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='inscricao_estadual',
            field=models.CharField(max_length=20, verbose_name='Inscrição Estadual'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='inscricao_municipal',
            field=models.CharField(max_length=20, verbose_name='Inscrição Municipal'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.PessoaFisica', verbose_name='Responsável'),
        ),
        migrations.AlterField(
            model_name='formaspagamentos',
            name='descricao',
            field=models.CharField(max_length=20, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='formaspagamentos',
            name='id_forma_pagamento',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Forma de Pagamento'),
        ),
        migrations.AlterField(
            model_name='fornecedorpessoafisica',
            name='cliente_fpf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.PessoaFisica', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='fornecedorpessoajuridica',
            name='cliente_fpj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.PessoaJuridica', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='lancamentospagar',
            name='data_emissao',
            field=models.DateField(default=datetime.date.today, help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>', verbose_name='Data de Emissão'),
        ),
        migrations.AlterField(
            model_name='lancamentospagar',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.Empresa', verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='lancamentospagar',
            name='fornecedor',
            field=models.ForeignKey(on_delete=financeiro.models.FornecedorPessoaJuridica, related_name='+', to='financeiro.FornecedorPessoaFisica', verbose_name='Fornecedor'),
        ),
        migrations.AlterField(
            model_name='lancamentospagar',
            name='id_lancamentos_pagar',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Identificação do Lançamento a Pagar'),
        ),
        migrations.AlterField(
            model_name='lancamentospagar',
            name='numero_documento',
            field=models.CharField(max_length=20, verbose_name='Número de Documento'),
        ),
        migrations.AlterField(
            model_name='lancamentosreceber',
            name='cliente',
            field=models.ForeignKey(on_delete=financeiro.models.ClientePessoaFisica, related_name='+', to='financeiro.ClientePessoaJuridica', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='lancamentosreceber',
            name='data_emissao',
            field=models.DateField(default=datetime.date.today, help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>', verbose_name='Data de Emissão'),
        ),
        migrations.AlterField(
            model_name='lancamentosreceber',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.Empresa', verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='lancamentosreceber',
            name='id_lancamentos_receber',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Identificação do Lançamento a Receber'),
        ),
        migrations.AlterField(
            model_name='lancamentosreceber',
            name='numero_documento',
            field=models.CharField(max_length=20, verbose_name='Número do Documento'),
        ),
        migrations.AlterField(
            model_name='lancamentosreceber',
            name='valor_titulo',
            field=models.FloatField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>', verbose_name='Valor do Título'),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='bairro',
            field=models.CharField(default='', max_length=50, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='cep',
            field=models.CharField(default=' ', help_text='Nao use caracteres especiais: <em>40353111</em', max_length=20, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='cpf',
            field=models.CharField(help_text='Use o seguinte formato: <em>xxx.xxx.xxx-xx</em>', max_length=15, primary_key=True, serialize=False, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='data_nascimento',
            field=models.DateField(default=datetime.date.today, help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>', verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='email',
            field=models.EmailField(default='', max_length=50, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='endereco',
            field=models.CharField(default='', max_length=50, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='funcao',
            field=models.CharField(max_length=49, verbose_name='Funçao'),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='municipio',
            field=models.CharField(default='', max_length=50, verbose_name='Município'),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='nome',
            field=models.CharField(default='', max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='sobrenome',
            field=models.CharField(default='', max_length=100, verbose_name='Sobrenome'),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='telefone',
            field=models.CharField(default='', help_text='Use o seguinte formato: <em>071999998888 ou 32220000</em>', max_length=20, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='uf',
            field=models.CharField(default='', max_length=2, verbose_name='UF'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='bairro',
            field=models.CharField(default='', max_length=50, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='cep',
            field=models.CharField(default=' ', help_text='Nao use caracteres especiais: <em>40353111</em', max_length=20, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='cnpj',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='email',
            field=models.EmailField(default='', max_length=50, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='endereco',
            field=models.CharField(default='', max_length=50, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='municipio',
            field=models.CharField(default='', max_length=50, verbose_name='Município'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='nome',
            field=models.CharField(default='', max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='razao_social',
            field=models.CharField(max_length=45, verbose_name='Razão Social'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='sobrenome',
            field=models.CharField(default='', max_length=100, verbose_name='Sobrenome'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='telefone',
            field=models.CharField(default='', help_text='Use o seguinte formato: <em>071999998888 ou 32220000</em>', max_length=20, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='uf',
            field=models.CharField(default='', max_length=2, verbose_name='UF'),
        ),
        migrations.AlterField(
            model_name='planodecontas',
            name='banco',
            field=models.CharField(max_length=20, verbose_name='Banco'),
        ),
        migrations.AlterField(
            model_name='planodecontas',
            name='caixa',
            field=models.CharField(max_length=20, verbose_name='Caixa'),
        ),
        migrations.AlterField(
            model_name='planodecontas',
            name='classificacao',
            field=models.CharField(max_length=20, verbose_name='Classificação'),
        ),
        migrations.AlterField(
            model_name='planodecontas',
            name='cliente',
            field=models.CharField(max_length=20, verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='planodecontas',
            name='contas_bancarias',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.ContasBancarias', verbose_name='Contas Bancárias'),
        ),
        migrations.AlterField(
            model_name='planodecontas',
            name='descricao',
            field=models.CharField(max_length=20, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='planodecontas',
            name='entrada_recurso',
            field=models.CharField(max_length=20, verbose_name='Entrada do Recurso'),
        ),
        migrations.AlterField(
            model_name='planodecontas',
            name='fornecedor',
            field=models.CharField(max_length=20, verbose_name='Fornecedeor'),
        ),
        migrations.AlterField(
            model_name='planodecontas',
            name='id_plano_contas',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Identificação'),
        ),
        migrations.AlterField(
            model_name='planodecontas',
            name='saida_recurso',
            field=models.CharField(max_length=20, verbose_name='Saída do Recurso'),
        ),
        migrations.AlterField(
            model_name='planodecontas',
            name='tipo_conta',
            field=models.CharField(max_length=20, verbose_name='Tipo da conta'),
        ),
        migrations.AlterField(
            model_name='tesouraria',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.ClientePessoaJuridica', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='tesouraria',
            name='conta_entrada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.ContasBancarias', verbose_name='Conta de Entrada'),
        ),
        migrations.AlterField(
            model_name='tesouraria',
            name='conta_saida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.ContasBancarias', verbose_name='Conta de Saída'),
        ),
        migrations.AlterField(
            model_name='tesouraria',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.Empresa', verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='tesouraria',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.FornecedorPessoaJuridica', verbose_name='Fornecedor'),
        ),
    ]
