from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.response import Response

from django.shortcuts import get_object_or_404


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = CLienteSerializer

class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

class MovimentacaoViewSet(viewsets.ModelViewSet):
    
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer

    def create(self, request, *args, **kwargs):
        dados_da_transacao = request.data 
        
        valor_da_transacao = float(dados_da_transacao['valor'])
        
        codigo_cliente_pagar = dados_da_transacao['cliente_pagar']
        codigo_cliente_receber = dados_da_transacao['cliente_receber']
        
        conta_pagar = get_object_or_404(Cliente, pk=codigo_cliente_pagar)
        conta_receber = get_object_or_404(Cliente, pk=codigo_cliente_receber)

        if conta_pagar.saldo <= valor_da_transacao : 
            print('não possui saldo suficiente')
            return Response({'movimentacao': f'não possui saldo suficiente'}, status=403)
    
        
        movimentacao = Movimentacao.objects.create(
            valor = valor_da_transacao,
            cliente_pagar = conta_pagar,
            cliente_receber = conta_receber
        )
        
        
        conta_pagar.saldo -= valor_da_transacao
        conta_receber.saldo += valor_da_transacao
        
        conta_pagar.save()
        conta_receber.save()
        print('deu certo')
        return Response({'movimentacao': f'criada com sucesso'}, status=status.HTTP_201_CREATED)
    
            


class InvestimentoViewSet(viewsets.ModelViewSet):
    queryset = Investimento.objects.all()
    serializer_class = InvestimentoSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class EmpretimoParcelaViewSet(viewsets.ModelViewSet):
    queryset = EmprestimoParcela.objects.all()
    serializer_class = EmprestimoParcelaSerializer