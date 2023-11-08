from rest_framework import serializers
from .models import *

class CLienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'codigo', 'usuario', 'foto_logo', 'senha', 'data_nascimento', 'data_abertura', 'nome_razaoSocial', 'nomeSocial_fantasia', 'cnpj',
            'inscricao_estadual', 'inscricao_municipal', 'rg', 'cpf', 'cliente_tipo'
        ]
     
"""
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = [
            'codigo', 'bairro', 'logradouro', 'cidade', 'cep', 'uf', 'fk_codigo_cliente'
        ]


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = [
            'codigo', 'observacao', 'email', 'ramal', 'numero', 'fk_codigo_cliente'
        ]


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = [
            'codigo', 'agencia', 'numero', 'limite', 'tipo', 'ativa', 'fk_codigo_cliente'
        ]
"""

class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = [
            'codigo', 'situacao', 'bandeira', 'numero', 'cvv', 'validade', 'fk_codigo_conta',
        ]


class MovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = [
            'codigo', 'operacao', 'data_Hora', 'valor', 'fk_codigo_cartao'
        ]


class InvestimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investimento
        fields = [
            'codigo', 'grauRisco', 'finalizado', 'rentabilidade', 'aporte', 'tipo', 'prazo', 'taxa_administracao', 'fk_codigo_conta'
        ]


class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = [
            'codigo', 'juros', 'numero_parcela', 'data_solicitacao', 'data_aprovacao', 'aprovado', 'valor_solicitado', 'observacao', 'fk_codigo_conta'
        ]


class EmprestimoParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmprestimoParcela
        fields = [
            'codigo', 'data_vencimento', 'valor_parcela', 'numero', 'data_pagamento', 'valor_pago', 'fk_codigo_emprestimo'
        ]
