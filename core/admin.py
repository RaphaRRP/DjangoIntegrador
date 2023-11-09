from django.contrib import admin
from .models import *

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'usuario', 'foto_logo', 'senha', 'data_nascimento', 'data_abertura',     'rg', 'cpf_cnpj', 'cliente_tipo', 'cep', 'numero', 'email', 'saldo'
        ]

@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'bandeira', 'validade', 'Codigo_Cliente'
        ]
    
@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'operacao', 'data_Hora', 'valor', 'Codigo_Cliente'
        ]
    
@admin.register(Investimento)
class InvestimentoAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'grauRisco','rentabilidade','Codigo_Cliente'
        ]
    
@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'juros', 'numero_parcela','valor_solicitado', 'Codigo_Cliente'
        ]
    
@admin.register(EmprestimoParcela)
class EmprestimoParcelaAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'data_vencimento', 'valor_parcela', 'pago', 'Codigo_Emprestimo'
        ]
    

    

    

    