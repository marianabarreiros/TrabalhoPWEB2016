# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 15:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0003_auto_20170513_1112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baixaspagar',
            options={'verbose_name': 'Baixa a Pagar', 'verbose_name_plural': 'Baixas a Pagar'},
        ),
        migrations.AlterModelOptions(
            name='baixasreceber',
            options={'verbose_name': 'Baixa a Receber', 'verbose_name_plural': 'Baixas a Receber'},
        ),
        migrations.AlterModelOptions(
            name='clientepessoafisica',
            options={'verbose_name': 'Cliente Pessoa Física', 'verbose_name_plural': 'Clientes Pessoa Física'},
        ),
        migrations.AlterModelOptions(
            name='clientepessoajuridica',
            options={'verbose_name': 'Cliente Pessoa Jurídica', 'verbose_name_plural': 'Clientes Pessoa Jurídica'},
        ),
        migrations.AlterModelOptions(
            name='contasbancarias',
            options={'verbose_name': 'Baixa a Receber', 'verbose_name_plural': 'Baixas a Receber'},
        ),
        migrations.AlterModelOptions(
            name='empresa',
            options={'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
        migrations.AlterModelOptions(
            name='formaspagamentos',
            options={'verbose_name': 'Forma de Pagamento', 'verbose_name_plural': 'Formas de Pagamento'},
        ),
        migrations.AlterModelOptions(
            name='fornecedorpessoafisica',
            options={'verbose_name': 'Fornecedor Físico', 'verbose_name_plural': 'Fornecedores Físicos'},
        ),
        migrations.AlterModelOptions(
            name='fornecedorpessoajuridica',
            options={'verbose_name': 'Fornecedor Júridico', 'verbose_name_plural': 'Fornecedores Júridicos'},
        ),
        migrations.AlterModelOptions(
            name='lancamentospagar',
            options={'verbose_name': 'Laçamento a Pagar', 'verbose_name_plural': 'Laçamentos a Pagar'},
        ),
        migrations.AlterModelOptions(
            name='lancamentosreceber',
            options={'verbose_name': 'Laçamento a Receber', 'verbose_name_plural': 'Laçamentos a Receber'},
        ),
        migrations.AlterModelOptions(
            name='pessoafisica',
            options={'verbose_name': 'Pessoa Física', 'verbose_name_plural': 'Pessoas Física'},
        ),
        migrations.AlterModelOptions(
            name='pessoajuridica',
            options={'verbose_name': 'Pessoa Jurídica', 'verbose_name_plural': 'Pessoas Jurídica'},
        ),
        migrations.AlterModelOptions(
            name='planodecontas',
            options={'verbose_name': 'Baixa a Receber', 'verbose_name_plural': 'Baixas a Receber'},
        ),
        migrations.AlterModelOptions(
            name='tesouraria',
            options={'verbose_name': 'Tesouraria', 'verbose_name_plural': 'Tesourarias'},
        ),
    ]
