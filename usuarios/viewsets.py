from rest_framework import viewsets,mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Usuario
from.serializers import UsuarioSerializer,UsuarioLoginSerializer,UsuarioRegisterSerializer


class UsuarioViewSet(mixins.ListModelMixin,viewsets.GenericViewset):
    queryset=Usuario.objects.all()

    serializer_class=UsuarioSerializer

    @action(detail=False,methids=['post'])
    def login(self,request):
        serializer=UsuarioLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()
        data={
            'Usuario':UsuarioSerializer(usuario).data
        }
        return Response(data)

    @action(detail=False,methods=['post'])
    def register(self,request):
        serializer=UsuarioRegisterSerializer(data=request.data)
        Usuario = serializer.save()
        data = UsuarioSerializer(Usuario).data
        return Response(data)