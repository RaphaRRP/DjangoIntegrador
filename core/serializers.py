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
    
    #def create(self, validated_data):
    #    conta_cli = validated_data.pop('Codigo_Cliente')
    #    cliente_instance = Cliente.objects.get_or_create(usuario=conta_cli)
    #    transacao_instance = Movimentacao.objects.create(**validated_data, Codigo_Cliente=cliente_instance)
    #    return transacao_instance


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
            'codigo', 'juros', 'numero_parcela','valor_solicitado', 'Codigo_Cliente'
        ]


class EmprestimoParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmprestimoParcela
        fields = [
            'codigo', 'data_vencimento', 'valor_parcela', 'pago', 'Codigo_Emprestimo'
        ]
