from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from time import sleep


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = CLienteSerializer

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


class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = cartaoSerializer

    
    def partial_update(self, request, *args, **kwargs):

        conta = self.get_object()

        if conta.cartao == True:
            return Response({'Emprestimo': f'Só é possivel solicitar um cartão'}, status=403)

        conta.cartao = True
        conta.save()
        return Response({'Cartão': f'Seu cartão foi solicitado com sucesso e chegará em sua residencia em breve! Cep: {conta.cep}'}, status=201)
    

tentativas = 0
class LoginViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        
        global tentativas 
        dados = request.data
        usuario_inserido = dados['usuario']
        senha_inserida = dados['senha']
        codigo_inserido = dados['codigo']

        cliente_logar = get_object_or_404(Cliente, pk=codigo_inserido)

        if usuario_inserido == cliente_logar.usuario and senha_inserida == cliente_logar.senha:
            tentativas  = 0
            return Response({'Login': 'Sucesso','Codigo': f'{codigo_inserido}' ,'Usuario': f'{usuario_inserido}'}, status=201)
        
        tentativas  += 1
        print(tentativas )

        if tentativas  > 3:
            sleep(20)
            return Response({'Não foi possivel realizar o login'}, status=403)
    
        if tentativas  == 1:
            return Response({'Não foi possivel realizar o login, tentativas restantes: 3'}, status=403)
        
        if tentativas  == 2:
            return Response({'Não foi possivel realizar o login, tentativas restantes: 2'}, status=403)
        
        if tentativas  == 3:
            return Response({'Não foi possivel realizar o login, tentativas restantes: 1'}, status=403)

