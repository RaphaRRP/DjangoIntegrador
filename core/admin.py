from django.contrib import admin
from .models import *

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'usuario', 'foto_logo', 'senha', 'data_nascimento', 'data_abertura','rg', 'cpf_cnpj', 'cliente_tipo', 'cep', 'numero', 'email', 'saldo', 'emprestimo'
        ]

@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'bandeira', 'validade', 'Codigo_Cliente'
        ]
    
@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'data_Hora', 'valor', 'cliente_pagar', 'cliente_receber'
        ]
    
@admin.register(Investimento)
class InvestimentoAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'grauRisco','rentabilidade','Codigo_Cliente'
        ]
    
@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'valor_solicitado', 'Codigo_Cliente'
        ]
    

    

    

    

    