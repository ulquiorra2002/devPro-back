from rest_framework import viewsets,mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Usuario
from.serializers import UsuarioSerializer,UsuarioLoginSerializer,UsuarioRegisterSerializer


class UsuarioViewSet(mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset=Usuario.objects.all()

    def get_serializer_class(self):
        if self.action =='register':
            return UsuarioRegisterSerializer
        if self.action in ['update','partial_update']:
            return UsuarioRegisterSerializer
        if self.action=='login':
            return UsuarioLoginSerializer
        return UsuarioSerializer

    @action(detail=False,methods=['post'])
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
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()
        data = UsuarioSerializer(usuario).data
        return Response(data)