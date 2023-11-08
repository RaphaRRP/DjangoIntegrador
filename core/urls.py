from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *


router = SimpleRouter()
router.register('cliente', ClienteViewSet)
#router.register('contato', ContatoViewSet)
#router.register('endereco', EnderecoViewSet)
#router.register('conta', ContaViewSet)
router.register('movimentacao', MovimentacaoViewSet)
router.register('investimento', InvestimentoViewSet)
router.register('emprestimo', EmprestimoViewSet)
router.register('parcela', EmpretimoParcelaViewSet)

"""
urlpatterns = [
    path('cliente/', views.ClientesAPIView.as_view(), name='clientes'),
    path('cliente/<int:pk>', views.ClienteAPIView.as_view(), name='cliente'),

    path('contato/', views.ContatosAPIView.as_view(), name='contatos'),
    path('contato/<int:pk>', views.ContatoAPIView.as_view(), name='contato'),

    path('endereco/', views.EnderecosAPIView.as_view(), name='enderecos'),
    path('endereco/<int:pk>', views.EnderecoAPIView.as_view(), name='endereco'),

    path('conta/', views.ContasAPIView.as_view, name='contas'),
    path('conta/<int:pk>', views.ContaAPIView.as_view, name='conta'),

    path('cartao/', views.CartoesAPIView.as_view(), name='cartoes'),
    path('cartao/<int:pk>', views.CartaoAPIView.as_view(), name='cartao'),

    path('movimentacao/', views.MovimentacoesAPIView.as_view(), name='movimentacoes'),
    path('movimentacao/<int:pk>', views.MovimentacaoAPIView.as_view(), name='movimentacao'),

    path('investimento/', views.InvestimentosAPIView.as_view(), name='investimentos'),
    path('investimento/<int:pk>', views.InvestimentoAPIView.as_view(), name='investimento'),

    path('emprestimo/', views.EmprestimosAPIView.as_view(), name='emprestimos'),
    path('emprestimo/<int:pk>', views.EmprestimoAPIView.as_view(), name='emprestimo'),

    path('parcelas/', views.EmpretimoParcelasAPIView.as_view(), name='parcelas'),
    path('parcelas/<int:pk>', views.EmpretimoParcelaAPIView.as_view(), name='parcela'),

    #==================================================================#

]
"""