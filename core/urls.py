from django.urls import path
from .views import ClienteAPIView

urlpatterns = [
    path('clientes/', ClienteAPIView.as_view(), name='clientes')
]
