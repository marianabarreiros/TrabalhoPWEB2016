from django.contrib import admin
from .models import *

admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(ClientePessoaFisica)
admin.site.register(ClientePessoaJuridica)
admin.site.register(Empresa)
admin.site.register(FornecedorPessoaFisica)
admin.site.register(FornecedorPessoaJuridica)

