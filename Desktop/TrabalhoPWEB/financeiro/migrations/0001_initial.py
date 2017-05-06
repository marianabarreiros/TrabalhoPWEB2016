# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=20)),
                ('uf', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='financeiro.Pessoa')),
                ('cpf', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('funcao', models.CharField(max_length=50)),
            ],
            bases=('financeiro.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='financeiro.Pessoa')),
                ('cnpj', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('razao_social', models.CharField(max_length=45)),
            ],
            bases=('financeiro.pessoa',),
        ),
        migrations.CreateModel(
            name='ClientePessoaFisica',
            fields=[
                ('pessoafisica_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, primary_key=True, to='financeiro.PessoaFisica')),
            ],
            bases=('financeiro.pessoafisica',),
        ),
        migrations.CreateModel(
            name='ClientePessoaJuridica',
            fields=[
                ('pessoajuridica_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, primary_key=True, to='financeiro.PessoaJuridica')),
            ],
            bases=('financeiro.pessoajuridica',),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('pessoajuridica_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, primary_key=True, to='financeiro.PessoaJuridica')),
                ('incricao_estadual', models.CharField(max_length=20)),
                ('inscricao_municipal', models.CharField(max_length=20)),
            ],
            bases=('financeiro.pessoajuridica',),
        ),
        migrations.CreateModel(
            name='FornecedorPessoaFisica',
            fields=[
                ('pessoafisica_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, primary_key=True, to='financeiro.PessoaFisica')),
                ('cliente', models.ForeignKey(to='financeiro.PessoaFisica', related_name='+')),
            ],
            bases=('financeiro.pessoafisica',),
        ),
        migrations.CreateModel(
            name='FornecedorPessoaJuridica',
            fields=[
                ('pessoajuridica_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, primary_key=True, to='financeiro.PessoaJuridica')),
                ('cliente', models.ForeignKey(to='financeiro.PessoaJuridica', related_name='+')),
            ],
            bases=('financeiro.pessoajuridica',),
        ),
        migrations.AddField(
            model_name='empresa',
            name='responsavel',
            field=models.ForeignKey(to='financeiro.PessoaFisica', related_name='+'),
        ),
        migrations.AddField(
            model_name='clientepessoajuridica',
            name='cnpj_do_vendedor',
            field=models.ForeignKey(to='financeiro.PessoaJuridica', related_name='+'),
        ),
        migrations.AddField(
            model_name='clientepessoafisica',
            name='cpf_do_vendedor',
            field=models.ForeignKey(to='financeiro.PessoaFisica', related_name='+'),
        ),
    ]
