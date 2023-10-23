from django.urls import path
from .views import ClienteAPIView, ClientesAPIView, ContatosAPIView, ContatoAPIView, EnderecosAPIView, EnderecoAPIView, ContasAPIView, ContaAPIView, CartoesAPIView, CartaoAPIView, MovimentacoesAPIView, MovimentacaoAPIView, InvestimentosAPIView, InvestimentoAPIView, EmprestimosAPIView, EmprestimoAPIView, EmpretimoParcelasAPIView, EmpretimoParcelaAPIView


urlpatterns = [
    path('cliente/', ClientesAPIView.as_view(), name='clientes'),
    path('cliente/<int:pk>', ClienteAPIView.as_view(), name='cliente'),

    path('contato/', ContatosAPIView.as_view(), name='contatos'),
    path('contato/<int:pk>', ContatoAPIView.as_view(), name='contato'),

    path('endereco/', EnderecosAPIView.as_view(), name='enderecos'),
    path('endereco/<int:pk>', EnderecoAPIView.as_view(), name='endereco'),

    path('conta/', ContasAPIView.as_view, name='contas'),
    path('conta/<int:pk>', ContaAPIView.as_view, name='conta'),

    path('cartao/', CartoesAPIView.as_view(), name='cartoes'),
    path('cartao/<int:pk>', CartaoAPIView.as_view(), name='cartao'),

    path('movimentacao/', MovimentacoesAPIView.as_view(), name='movimentacoes'),
    path('movimentacao/<int:pk>', MovimentacaoAPIView.as_view(), name='movimentacao'),

    path('investimento/', InvestimentosAPIView.as_view(), name='investimentos'),
    path('investimento/<int:pk>', InvestimentoAPIView.as_view(), name='investimento'),

    path('emprestimo/', EmprestimosAPIView.as_view(), name='emprestimos'),
    path('emprestimo/<int:pk>', EmprestimoAPIView.as_view(), name='emprestimo'),

    path('parcelas/', EmpretimoParcelasAPIView.as_view(), name='parcelas'),
    path('parcelas/<int:pk>', EmpretimoParcelaAPIView.as_view(), name='parcela')



]
