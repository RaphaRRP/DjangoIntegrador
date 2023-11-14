from rest_framework import serializers
from .models import *

class CLienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'codigo', 'usuario', 'senha', 'data_abertura', 'cpf_cnpj', 'cep', 'numero', 'email', 'saldo', 'emprestimo', 'cartao', 'image'
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

class cartaoSerializer(serializers.Serializer):
    codigo = serializers.CharField()

class LoginSerializer(serializers.Serializer):
    class Meta:
        model = Cliente
        fields = [
            'codigo', 'usuario', 'senha'
        ]
    


