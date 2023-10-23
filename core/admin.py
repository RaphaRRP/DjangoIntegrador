from django.contrib import admin
from .models import Contato, Cliente, Endereco, Conta, Cartao, Movimentacao, Investimento, Emprestimo, EmprestimoParcela

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'usuario', 'foto_logo', 'senha', 'data_nascimento', 'data_abertura', 'nome_razaoSocial', 'nomeSocial_fantasia', 'cnpj','inscricao_estadual', 'inscricao_municipal', 'rg', 'cpf', 'cliente_tipo'
        ]

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'bairro', 'logradouro', 'cidade', 'cep', 'uf', 'fk_codigo_cliente'
        ]

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'observacao', 'email', 'ramal', 'numero', 'fk_codigo_cliente'
        ]

@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'agencia', 'numero', 'limite', 'tipo', 'ativa', 'fk_codigo_cliente'
        ]
    
@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'situacao', 'bandeira', 'numero', 'cvv', 'validade', 'fk_codigo_conta'
        ]
    
@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'operacao', 'data_Hora', 'valor', 'fk_codigo_cartao'
        ]
    
@admin.register(Investimento)
class InvestimentoAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'grauRisco', 'finalizado', 'rentabilidade', 'aporte', 'tipo', 'prazo', 'taxa_administracao', 'fk_codigo_conta'
        ]
    
@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'juros', 'numero_parcela', 'data_solicitacao', 'data_aprovacao', 'aprovado', 'valor_solicitado', 'observacao', 'fk_codigo_conta'
        ]
    
@admin.register(EmprestimoParcela)
class EmprestimoParcelaAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'data_vencimento', 'valor_parcela', 'numero', 'data_pagamento', 'valor_pago', 'fk_codigo_emprestimo'
        ]
    

    

    

    