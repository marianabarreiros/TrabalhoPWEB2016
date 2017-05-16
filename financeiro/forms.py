from django import forms
from .models import LancamentosReceber


class LancamentoReceberForm(forms.ModelForm):
    class Meta:
        model = LancamentosReceber
        fiels = ('id_lancamentos_receber', 'clienteFisico', 'clienteJuridico', 'empresa', 'data_vencimento', 'data_emissao', 'valor_titulo', 'numero_documento')