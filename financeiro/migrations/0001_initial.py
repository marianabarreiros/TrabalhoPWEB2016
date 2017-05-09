# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import financeiro.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaixasPagar',
            fields=[
                ('id_baixa_pagar', models.CharField(serialize=False, primary_key=True, max_length=10)),
                ('banco', models.CharField(max_length=20)),
                ('disponibilidade', models.CharField(max_length=20)),
                ('data_baixa', models.DateField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>')),
                ('residual', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='BaixasReceber',
            fields=[
                ('id_baixa_receber', models.CharField(serialize=False, primary_key=True, max_length=10)),
                ('banco', models.CharField(max_length=20)),
                ('disponibilidade', models.CharField(max_length=20)),
                ('data_baixa', models.DateField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>')),
                ('residual', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ContasBancarias',
            fields=[
                ('id_contas_bancarias', models.IntegerField(serialize=False, primary_key=True)),
                ('classificacao', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=20)),
                ('numero_conta', models.CharField(max_length=20)),
                ('numero_agencia', models.CharField(max_length=20)),
                ('data_saldo_inicial', models.DateField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>')),
                ('caixa', models.CharField(max_length=20)),
                ('banco', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FormasPagamentos',
            fields=[
                ('id_forma_pagamento', models.CharField(serialize=False, primary_key=True, max_length=10)),
                ('descricao', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LancamentosPagar',
            fields=[
                ('id_lancamentos_pagar', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('data_emissao', models.DateField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>')),
                ('numero_documento', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LancamentosReceber',
            fields=[
                ('id_lancamentos_receber', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('data_emissao', models.DateField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>')),
                ('valor_titulo', models.FloatField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>')),
                ('numero_documento', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=20, help_text='Nao use caracteres especiais: <em>40353111</em')),
                ('uf', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=20, help_text='Use o seguinte formato: <em>071999998888 ou 32220000</em>')),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PlanoDeContas',
            fields=[
                ('id_plano_contas', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('classificacao', models.CharField(max_length=20)),
                ('tipo_conta', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=20)),
                ('caixa', models.CharField(max_length=20)),
                ('banco', models.CharField(max_length=20)),
                ('cliente', models.CharField(max_length=20)),
                ('fornecedor', models.CharField(max_length=20)),
                ('entrada_recurso', models.CharField(max_length=20)),
                ('saida_recurso', models.CharField(max_length=20)),
                ('contas_bancarias', models.ForeignKey(related_name='+', to='financeiro.ContasBancarias')),
            ],
        ),
        migrations.CreateModel(
            name='Tesouraria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('conta_entrada', models.ForeignKey(related_name='+', to='financeiro.ContasBancarias')),
                ('conta_saida', models.ForeignKey(related_name='+', to='financeiro.ContasBancarias')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, to='financeiro.Pessoa', parent_link=True)),
                ('cpf', models.CharField(serialize=False, primary_key=True, max_length=15, help_text='Use o seguinte formato: <em>xxx.xxx.xxx-xx</em>')),
                ('data_nascimento', models.DateField(help_text='Use o seguinte formato: <em>DD/MM/AAAA</em>')),
                ('funcao', models.CharField(max_length=50)),
            ],
            bases=('financeiro.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, to='financeiro.Pessoa', parent_link=True)),
                ('cnpj', models.CharField(serialize=False, primary_key=True, max_length=15)),
                ('razao_social', models.CharField(max_length=45)),
            ],
            bases=('financeiro.pessoa',),
        ),
        migrations.AddField(
            model_name='baixasreceber',
            name='id_forma_pagamento',
            field=models.ForeignKey(related_name='+', to='financeiro.FormasPagamentos'),
        ),
        migrations.AddField(
            model_name='baixasreceber',
            name='id_lancamentos_receber',
            field=models.ForeignKey(related_name='+', to='financeiro.LancamentosReceber'),
        ),
        migrations.AddField(
            model_name='baixaspagar',
            name='id_forma_pagamento',
            field=models.ForeignKey(related_name='+', to='financeiro.FormasPagamentos'),
        ),
        migrations.AddField(
            model_name='baixaspagar',
            name='id_lancamentos_pagar',
            field=models.ForeignKey(related_name='+', to='financeiro.LancamentosPagar'),
        ),
        migrations.CreateModel(
            name='ClientePessoaFisica',
            fields=[
                ('pessoafisica_ptr', models.OneToOneField(primary_key=True, to='financeiro.PessoaFisica', serialize=False, parent_link=True, auto_created=True)),
            ],
            bases=('financeiro.pessoafisica',),
        ),
        migrations.CreateModel(
            name='ClientePessoaJuridica',
            fields=[
                ('pessoajuridica_ptr', models.OneToOneField(primary_key=True, to='financeiro.PessoaJuridica', serialize=False, parent_link=True, auto_created=True)),
            ],
            bases=('financeiro.pessoajuridica',),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('pessoajuridica_ptr', models.OneToOneField(primary_key=True, to='financeiro.PessoaJuridica', serialize=False, parent_link=True, auto_created=True)),
                ('inscricao_estadual', models.CharField(max_length=20)),
                ('inscricao_municipal', models.CharField(max_length=20)),
            ],
            bases=('financeiro.pessoajuridica',),
        ),
        migrations.CreateModel(
            name='FornecedorPessoaFisica',
            fields=[
                ('pessoafisica_ptr', models.OneToOneField(primary_key=True, to='financeiro.PessoaFisica', serialize=False, parent_link=True, auto_created=True)),
                ('cliente', models.ForeignKey(related_name='+', to='financeiro.PessoaFisica')),
            ],
            bases=('financeiro.pessoafisica',),
        ),
        migrations.CreateModel(
            name='FornecedorPessoaJuridica',
            fields=[
                ('pessoajuridica_ptr', models.OneToOneField(primary_key=True, to='financeiro.PessoaJuridica', serialize=False, parent_link=True, auto_created=True)),
                ('cliente', models.ForeignKey(related_name='+', to='financeiro.PessoaJuridica')),
            ],
            bases=('financeiro.pessoajuridica',),
        ),
        migrations.AddField(
            model_name='tesouraria',
            name='cliente',
            field=models.ForeignKey(related_name='+', to='financeiro.ClientePessoaJuridica'),
        ),
        migrations.AddField(
            model_name='tesouraria',
            name='empresa',
            field=models.ForeignKey(related_name='+', to='financeiro.Empresa'),
        ),
        migrations.AddField(
            model_name='tesouraria',
            name='fornecedor',
            field=models.ForeignKey(related_name='+', to='financeiro.FornecedorPessoaJuridica'),
        ),
        migrations.AddField(
            model_name='lancamentosreceber',
            name='cliente',
            field=models.ForeignKey(to='financeiro.ClientePessoaJuridica', related_name='+', to_field=financeiro.models.ClientePessoaFisica),
        ),
        migrations.AddField(
            model_name='lancamentosreceber',
            name='empresa',
            field=models.ForeignKey(related_name='+', to='financeiro.Empresa'),
        ),
        migrations.AddField(
            model_name='lancamentospagar',
            name='empresa',
            field=models.ForeignKey(related_name='+', to='financeiro.Empresa'),
        ),
        migrations.AddField(
            model_name='lancamentospagar',
            name='fornecedor',
            field=models.ForeignKey(to='financeiro.FornecedorPessoaFisica', related_name='+', to_field=financeiro.models.FornecedorPessoaJuridica),
        ),
        migrations.AddField(
            model_name='empresa',
            name='responsavel',
            field=models.ForeignKey(related_name='+', to='financeiro.PessoaFisica'),
        ),
        migrations.AddField(
            model_name='clientepessoajuridica',
            name='cnpj_do_vendedor',
            field=models.ForeignKey(related_name='+', to='financeiro.PessoaJuridica'),
        ),
        migrations.AddField(
            model_name='clientepessoafisica',
            name='cpf_do_vendedor',
            field=models.ForeignKey(related_name='+', to='financeiro.PessoaFisica'),
        ),
    ]
