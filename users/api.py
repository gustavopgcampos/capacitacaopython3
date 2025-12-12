from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .serializers import UserSerializer

# cria a api rest dos usuários protegida apenas para os administradores
class UsuarioViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create (self, request, *args, **kwargs):
        resposta = super().create(request, *args, **kwargs)

        return Response({
            "mensagem": "Usuário criado com sucesso", 
        }, status=status.HTTP_201_CREATED)
    
    def destroy (self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response({
            "mensagem": "Usuário deletado com sucesso"
        }, status=status.HTTP_200_OK)