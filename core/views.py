from rest_framework import generics
from .models import Cliente
from .serializers import CLienteSerializer

class ClienteAPIView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = CLienteSerializer

