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
        
        numero_da_conta = dados_da_transacao['Codigo_Cliente']
        
        
        cliente_conta = get_object_or_404(Cliente, pk=numero_da_conta)

        saldo = cliente_conta.saldo

        
        if saldo < (valor_da_transacao * -1): 
            return Response({'movimentacao': f'não foi criada'}, status=403)
    
        
        movimentacao = Movimentacao.objects.create(
            operacao = "+",
            valor= valor_da_transacao,
            Codigo_Cliente = cliente_conta
        )
        
        cliente_conta.saldo += valor_da_transacao
        cliente_conta.save()
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