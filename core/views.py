from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


"""
class ClientesAPIView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = CLienteSerializer
    permission_classes = (IsAuthenticated,)


class ClienteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = CLienteSerializer


class ContatosAPIView(generics.ListCreateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

class ContatoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer


class EnderecosAPIView(generics.ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class EnderecoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class ContasAPIView(generics.ListCreateAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class ContaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer


class CartoesAPIView(generics.ListCreateAPIView):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

class CartaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer


class MovimentacoesAPIView(generics.ListCreateAPIView):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer

class MovimentacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer


class InvestimentosAPIView(generics.ListCreateAPIView):
    queryset = Investimento.objects.all()
    serializer_class = InvestimentoSerializer

class InvestimentoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Investimento.objects.all()
    serializer_class = InvestimentoSerializer


class EmprestimosAPIView(generics.ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class EmprestimoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer


class EmpretimoParcelasAPIView(generics.ListCreateAPIView):
    queryset = EmprestimoParcela.objects.all()
    serializer_class = EmprestimoParcelaSerializer

class EmpretimoParcelaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmprestimoParcela.objects.all()
    serializer_class = EmprestimoParcelaSerializer

"""

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = CLienteSerializer
    #permission_classes = (IsAuthenticated,)
"""
#class ContatoViewSet(viewsets.ModelViewSet):
    #queryset = Contato.objects.all()
    #serializer_class = ContatoSerializer

#class EnderecoViewSet(viewsets.ModelViewSet):
    #queryset = Endereco.objects.all()
    #serializer_class = EnderecoSerializer

#class ContaViewSet(viewsets.ModelViewSet):
    #queryset = Conta.objects.all()
    #serializer_class = ContaSerializer
"""

class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

class MovimentacaoViewSet(viewsets.ModelViewSet):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer

class InvestimentoViewSet(viewsets.ModelViewSet):
    queryset = Investimento.objects.all()
    serializer_class = InvestimentoSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class EmpretimoParcelaViewSet(viewsets.ModelViewSet):
    queryset = EmprestimoParcela.objects.all()
    serializer_class = EmprestimoParcelaSerializer