# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 19:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import financeiro.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaixasPagar',
            fields=[
                ('id_baixa_pagar', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Identificação')),
                ('banco', models.CharField(max_length=20, verbose_name='Banco')),
                ('disponibilidade', models.CharField(max_length=20, verbose_name='Disponibilidade')),
                ('data_baixa', models.DateField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>', verbose_name='Data da Baixa')),
                ('valor_pago', models.FloatField(default=0, verbose_name='Valo Pago')),
                ('residual', models.CharField(max_length=20, verbose_name='Residual')),
            ],
            options={
                'verbose_name': 'Baixa a Pagar',
                'verbose_name_plural': 'Baixas a Pagar',
            },
        ),
        migrations.CreateModel(
            name='BaixasReceber',
            fields=[
                ('id_baixa_receber', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Identificação')),
                ('banco', models.CharField(max_length=20, verbose_name='Banco')),
                ('disponibilidade', models.CharField(max_length=20, verbose_name='Disponibilidade')),
                ('data_baixa', models.DateField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>', verbose_name='Data de Baixa')),
                ('valor_pago', models.FloatField(default='0', verbose_name='Valor Pago')),
                ('residual', models.CharField(max_length=20, verbose_name='Residual')),
            ],
            options={
                'verbose_name': 'Baixa a Receber',
                'verbose_name_plural': 'Baixas a Receber',
            },
        ),
        migrations.CreateModel(
            name='ContasBancarias',
            fields=[
                ('id_contas_bancarias', models.IntegerField(primary_key=True, serialize=False, verbose_name='Identificação')),
                ('classificacao', models.CharField(max_length=20, verbose_name='Classificação')),
                ('descricao', models.CharField(max_length=20, verbose_name='Descrição')),
                ('numero_conta', models.CharField(max_length=20, verbose_name='Número da Conta')),
                ('numero_agencia', models.CharField(max_length=20, verbose_name='Núemro da Agência')),
                ('data_saldo_inicial', models.DateField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>', verbose_name='Data do Saldo Inicial')),
                ('saldo_inicial', models.FloatField(default=0, verbose_name='Saldo Inicial')),
                ('caixa', models.CharField(max_length=20, verbose_name='Caixa')),
                ('banco', models.CharField(max_length=20, verbose_name='Banco')),
            ],
            options={
                'verbose_name': 'Conta Bancária',
                'verbose_name_plural': 'Contas Bancária',
            },
        ),
        migrations.CreateModel(
            name='FormasPagamentos',
            fields=[
                ('id_forma_pagamento', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Forma de Pagamento')),
                ('descricao', models.CharField(max_length=20, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Forma de Pagamento',
                'verbose_name_plural': 'Formas de Pagamento',
            },
        ),
        migrations.CreateModel(
            name='LancamentosPagar',
            fields=[
                ('id_lancamentos_pagar', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Identificação do Lançamento a Pagar')),
                ('data_vencimento', models.DateField(default=datetime.date.today, verbose_name='Data de Vencimento')),
                ('data_emissao', models.DateField(default=datetime.date.today, help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>', verbose_name='Data de Emissão')),
                ('valor_titulo', models.FloatField(default=0, verbose_name='Valor do Título')),
                ('numero_documento', models.CharField(max_length=20, verbose_name='Número de Documento')),
            ],
            options={
                'verbose_name': 'Laçamento a Pagar',
                'verbose_name_plural': 'Laçamentos a Pagar',
            },
        ),
        migrations.CreateModel(
            name='LancamentosReceber',
            fields=[
                ('id_lancamentos_receber', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Identificação do Lançamento a Receber')),
                ('data_vencimento', models.DateField(default=datetime.date.today, verbose_name='Data de Vencimento')),
                ('data_emissao', models.DateField(default=datetime.date.today, help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>', verbose_name='Data de Emissão')),
                ('valor_titulo', models.FloatField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>', verbose_name='Valor do Título')),
                ('numero_documento', models.CharField(max_length=20, verbose_name='Número do Documento')),
            ],
            options={
                'verbose_name': 'Laçamento a Receber',
                'verbose_name_plural': 'Laçamentos a Receber',
            },
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('endereco', models.CharField(default='', max_length=50, verbose_name='Endereço')),
                ('bairro', models.CharField(default='', max_length=50, verbose_name='Bairro')),
                ('municipio', models.CharField(default='', max_length=50, verbose_name='Município')),
                ('cep', models.CharField(default=' ', help_text='Nao use caracteres especiais: <em>40353111</em', max_length=20, verbose_name='CEP')),
                ('uf', models.CharField(default='', max_length=2, verbose_name='UF')),
                ('telefone', models.CharField(default='', help_text='Use o seguinte formato: <em>071999998888 ou 32220000</em>', max_length=20, verbose_name='Telefone')),
                ('email', models.EmailField(default='', max_length=50, verbose_name='E-mail')),
                ('nome', models.CharField(default='', max_length=50, verbose_name='Nome')),
                ('sobrenome', models.CharField(default='', max_length=100, verbose_name='Sobrenome')),
                ('cpf', models.CharField(help_text='Use o seguinte formato: <em>xxx.xxx.xxx-xx</em>', max_length=15, primary_key=True, serialize=False, verbose_name='CPF')),
                ('data_nascimento', models.DateField(default=datetime.date.today, help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>', verbose_name='Data de Nascimento')),
                ('funcao', models.CharField(max_length=49, verbose_name='Funçao')),
            ],
            options={
                'verbose_name': 'Pessoa Física',
                'verbose_name_plural': 'Pessoas Física',
            },
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('endereco', models.CharField(default='', max_length=50, verbose_name='Endereço')),
                ('bairro', models.CharField(default='', max_length=50, verbose_name='Bairro')),
                ('municipio', models.CharField(default='', max_length=50, verbose_name='Município')),
                ('cep', models.CharField(default=' ', help_text='Nao use caracteres especiais: <em>40353111</em', max_length=20, verbose_name='CEP')),
                ('uf', models.CharField(default='', max_length=2, verbose_name='UF')),
                ('telefone', models.CharField(default='', help_text='Use o seguinte formato: <em>071999998888 ou 32220000</em>', max_length=20, verbose_name='Telefone')),
                ('email', models.EmailField(default='', max_length=50, verbose_name='E-mail')),
                ('razao_social', models.CharField(max_length=45, verbose_name='Razão Social')),
                ('cnpj', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='CNPJ')),
            ],
            options={
                'verbose_name': 'Pessoa Jurídica',
                'verbose_name_plural': 'Pessoas Jurídica',
            },
        ),
        migrations.CreateModel(
            name='PlanoDeContas',
            fields=[
                ('id_plano_contas', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Identificação')),
                ('classificacao', models.CharField(max_length=20, verbose_name='Classificação')),
                ('tipo_conta', models.CharField(max_length=20, verbose_name='Tipo da conta')),
                ('descricao', models.CharField(max_length=20, verbose_name='Descrição')),
                ('caixa', models.CharField(max_length=20, verbose_name='Caixa')),
                ('banco', models.CharField(max_length=20, verbose_name='Banco')),
                ('cliente', models.CharField(max_length=20, verbose_name='Cliente')),
                ('fornecedor', models.CharField(max_length=20, verbose_name='Fornecedeor')),
                ('entrada_recurso', models.CharField(max_length=20, verbose_name='Entrada do Recurso')),
                ('saida_recurso', models.CharField(max_length=20, verbose_name='Saída do Recurso')),
                ('contas_bancarias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.ContasBancarias', verbose_name='Contas Bancárias')),
            ],
            options={
                'verbose_name': 'Baixa a Receber',
                'verbose_name_plural': 'Baixas a Receber',
            },
        ),
        migrations.CreateModel(
            name='Tesouraria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(default=0, verbose_name='Valor')),
                ('numero_documento', models.IntegerField(default=0, verbose_name='Númedo do Documnto')),
                ('data_emissao', models.DateField(default=datetime.date.today, verbose_name='Data de Emissão')),
                ('data_vencimento', models.DateField(default=datetime.date.today, verbose_name='Data de Vencimento')),
                ('data_disponibilidade', models.DateField(default=datetime.date.today, verbose_name='Data de Disponibilidade')),
                ('conta_entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.ContasBancarias', verbose_name='Conta de Entrada')),
                ('conta_saida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.ContasBancarias', verbose_name='Conta de Saída')),
            ],
            options={
                'verbose_name': 'Tesouraria',
                'verbose_name_plural': 'Tesourarias',
            },
        ),
        migrations.CreateModel(
            name='ClientePessoaFisica',
            fields=[
                ('pessoafisica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financeiro.PessoaFisica')),
            ],
            options={
                'verbose_name': 'Cliente Pessoa Física',
                'verbose_name_plural': 'Clientes Pessoa Física',
            },
            bases=('financeiro.pessoafisica',),
        ),
        migrations.CreateModel(
            name='ClientePessoaJuridica',
            fields=[
                ('pessoajuridica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financeiro.PessoaJuridica')),
            ],
            options={
                'verbose_name': 'Cliente Pessoa Jurídica',
                'verbose_name_plural': 'Clientes Pessoa Jurídica',
            },
            bases=('financeiro.pessoajuridica',),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('pessoajuridica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financeiro.PessoaJuridica')),
                ('inscricao_estadual', models.CharField(max_length=20, verbose_name='Inscrição Estadual')),
                ('inscricao_municipal', models.CharField(max_length=20, verbose_name='Inscrição Municipal')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
            bases=('financeiro.pessoajuridica',),
        ),
        migrations.CreateModel(
            name='FornecedorPessoaFisica',
            fields=[
                ('pessoafisica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financeiro.PessoaFisica')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.PessoaFisica', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Fornecedor Físico',
                'verbose_name_plural': 'Fornecedores Físicos',
            },
            bases=('financeiro.pessoafisica',),
        ),
        migrations.CreateModel(
            name='FornecedorPessoaJuridica',
            fields=[
                ('pessoajuridica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financeiro.PessoaJuridica')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.PessoaJuridica', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Fornecedor Júridico',
                'verbose_name_plural': 'Fornecedores Júridicos',
            },
            bases=('financeiro.pessoajuridica',),
        ),
        migrations.AddField(
            model_name='baixasreceber',
            name='id_forma_pagamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.FormasPagamentos', verbose_name='Forma de Pagamento'),
        ),
        migrations.AddField(
            model_name='baixasreceber',
            name='id_lancamentos_receber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.LancamentosReceber', verbose_name='Identificação Lançamento a Receber'),
        ),
        migrations.AddField(
            model_name='baixaspagar',
            name='id_forma_pagamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.FormasPagamentos', verbose_name='Forma de Pagamento'),
        ),
        migrations.AddField(
            model_name='baixaspagar',
            name='id_lancamentos_pagar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.LancamentosPagar', verbose_name='Identificaçao do Pagamento a Pagar'),
        ),
        migrations.AddField(
            model_name='tesouraria',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.ClientePessoaJuridica', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='tesouraria',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.Empresa', verbose_name='Empresa'),
        ),
        migrations.AddField(
            model_name='tesouraria',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.FornecedorPessoaJuridica', verbose_name='Fornecedor'),
        ),
        migrations.AddField(
            model_name='lancamentosreceber',
            name='cliente',
            field=models.ForeignKey(on_delete=financeiro.models.ClientePessoaFisica, related_name='+', to='financeiro.ClientePessoaJuridica', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='lancamentosreceber',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.Empresa', verbose_name='Empresa'),
        ),
        migrations.AddField(
            model_name='lancamentospagar',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.Empresa', verbose_name='Empresa'),
        ),
        migrations.AddField(
            model_name='lancamentospagar',
            name='fornecedor',
            field=models.ForeignKey(on_delete=financeiro.models.FornecedorPessoaJuridica, related_name='+', to='financeiro.FornecedorPessoaFisica', verbose_name='Fornecedor'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='financeiro.PessoaFisica', verbose_name='Responsável'),
        ),
    ]
