from django.contrib import admin
from .models import *

admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(ClientePessoaFisica)
admin.site.register(ClientePessoaJuridica)
admin.site.register(Empresa)
admin.site.register(FornecedorPessoaFisica)
admin.site.register(FornecedorPessoaJuridica)
admin.site.register(LancamentosReceber)
admin.site.register(LancamentosPagar)
admin.site.register(FormasPagamentos)
admin.site.register(BaixasReceber)
admin.site.register(BaixasPagar)
admin.site.register(ContasBancarias)
admin.site.register(PlanoDeContas)
admin.site.register(Tesouraria)


