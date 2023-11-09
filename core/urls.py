from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *


router = SimpleRouter()
router.register('cliente', ClienteViewSet)
router.register('movimentacao', MovimentacaoViewSet)
router.register('investimento', InvestimentoViewSet)
router.register('emprestimo', EmprestimoViewSet)
router.register('parcela', EmpretimoParcelaViewSet)

