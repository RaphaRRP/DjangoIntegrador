from rest_framework import serializers
from .models import *

class CLienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'codigo', 'usuario', 'foto_logo', 'senha', 'data_nascimento', 'data_abertura','rg', 'cpf_cnpj', 'cliente_tipo', 'cep', 'numero', 'email', 'saldo'
        ]

class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = [
            'codigo', 'bandeira', 'validade', 'Codigo_Cliente'
        ]


class MovimentacaoSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Movimentacao
        fields = [
            'codigo','data_Hora', 'valor', 'cliente_pagar', 'cliente_receber'
        ]
    

class InvestimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investimento
        fields = [
            'codigo', 'grauRisco','rentabilidade','Codigo_Cliente'
        ]


class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields =  [
            'codigo','valor_solicitado', 'Codigo_Cliente'
        ]

class PagarSerializer(serializers.Serializer):
    codigo = serializers.CharField()


