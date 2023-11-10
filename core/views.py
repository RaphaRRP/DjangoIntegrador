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
        return Response({'movimentacao': f'criada com sucesso'}, status=201)
    

class InvestimentoViewSet(viewsets.ModelViewSet):
    queryset = Investimento.objects.all()
    serializer_class = InvestimentoSerializer


class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    def create(self, request, *args, **kwargs):

        dados_do_emprestimo = request.data

        valor_do_emprestimo = float(dados_do_emprestimo['valor_solicitado'])

        codigo_cliente_emprestimo = dados_do_emprestimo['Codigo_Cliente']

        conta_emprestimo = get_object_or_404(Cliente, pk=codigo_cliente_emprestimo)


      
        if conta_emprestimo.emprestimo != 0:#apenas um emprestimo de cada vez
            return Response({'Emprestimo': f'Por favor, pague o empréstimo em aberto antes de realizar outro'}, status=403)


        if valor_do_emprestimo > (conta_emprestimo.saldo * 0.1):#emprestimo de no máximo 10% do saldo
            return Response({'Emprestimo': f'O valor do empréstimo deve ser no máximo 10% do saldo em sua conta'}, status=403)

        emprestimo = Emprestimo.objects.create(
            valor_solicitado = valor_do_emprestimo,
            Codigo_Cliente = conta_emprestimo
        )

        conta_emprestimo.saldo += valor_do_emprestimo
        conta_emprestimo.emprestimo = valor_do_emprestimo
        conta_emprestimo.save()

        return Response({'Emprestimo': f'Emprestimo de {valor_do_emprestimo} aceito com sucesso!'}, status=201)
    

class PagarEmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = PagarSerializer

    def partial_update(self, request, *args, **kwargs):

        conta = self.get_object()

        if conta.emprestimo == 0:
            return Response({'Emprestimo': f'Essa conta não possui emprestimo'}, status=403)

        if conta.emprestimo > conta.saldo:
            return Response({'Emprestimo': f'Não a saldo o suficiente para pagar o empréstimo'}, status=403)

        valor_emprestimo = conta.emprestimo
        conta.emprestimo = 0
        conta.saldo -= valor_emprestimo
        conta.save()
    
        return Response({'Emprestimo': f'Emprestimo de {valor_emprestimo} Pago com sucesso!'}, status=201)

        # conta_emprestimo = get_object_or_404(Cliente, pk=conta)
        
        # if conta_emprestimo.emprestimo > conta_emprestimo.saldo:
        #     return Response({'Emprestimo': f'Não a saldo o suficiente para pagar o empréstimo'}, status=403)

        #conta_emprestimo.emprestimo = 0
        # conta_emprestimo.saldo -= conta_emprestimo.emprestimo

        # return Response({'Emprestimo': f'Emprestimo de {conta_emprestimo.emprestimo} Pago com sucesso!'}, status=201)
