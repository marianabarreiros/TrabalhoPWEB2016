from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.tela_inicial, name='tela_inicial'),

    #Url's para o cadastro das informações
    url(r'^cadastro_cliente_fisico$', views.tela_cadastro_cliente_fisico, name='cadastro_cliente_fisico'),
    url(r'^cadastro_cliente_juridico$', views.tela_cadastro_cliente_juridico, name='cadastro_cliente_juridico'),
    url(r'^cadastro_empresa$', views.tela_cadastro_empresa, name='cadastro_empresa'),
    url(r'^cadastro_fornecedor_juridico$', views.tela_fornecedor_juridico, name='cadastro_fornecedor_juridico'),
    url(r'^cadastro_fornecedor_fisico$', views.tela_fornecedor_fisico, name='cadastro_fornecedor_fisico'),
    url(r'^cadastro_plano_de_conta$', views.tela_plano_de_conta, name='cadastro_plano_de_conta'),
    url(r'^cadastro_formas_de_pagamento$', views.tela_formas_de_pagamento, name='cadastro_formas_de_pagamento'),
    url(r'^cadastro_conta_bancaria$', views.tela_conta_bancaria, name='cadastro_conta_bancaria'),
    url(r'^cadastro_tesouraria$', views.tela_tesouraria, name='cadastro_tesouraria'),
    url(r'^cadastro_baixas_receber$', views.tela_baixas_receber, name='cadastro_baixas_receber'),
    url(r'^cadastro_baixas_pagar$', views.tela_baixas_pagar, name='cadastro_baixas_pagar'),
    url(r'^cadastro_lancamentos_pagar$', views.tela_lancamentos_pagar, name='cadastro_lancamentos_pagar'),
    url(r'^cadastro_lancamentos_receber$', views.tela_lancamentos_receber, name='cadastro_lancamentos_receber'),
    url(r'^lancamentos_receber_new$', views.lancamentos_receber, name='lancamentos_receber'),

    #Url's para o trazer as informações do relatório

    url(r'^recupera_contas_receber$', views.tela_recupera_contas_receber, name='recupera_contas_receber'),
    url(r'^recupera_contas_pagar$', views.tela_recupera_contas_pagar, name='recupera_contas_pagar'),
    url(r'^recupera_movimentos$', views.tela_recupera_movimentos, name='recupera_movimentos'),
    url(r'^recupera_fluxo_caixa$', views.tela_recupera_fluxo_caixa, name='recupera_fluxo_caixa'),




]
