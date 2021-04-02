from django.contrib.auth import authenticate,password_validation

from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields='__all__'

class UsuarioLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password=serializers.CharField()

    class Meta:
        model = Usuario
        fields=['email','password']

    def validate(self,data):
        usuario = authenticate(
            username=data['email'], password=data['password'])
        print(usuario)
        if not usuario:
            raise serializers.ValidationError('Credenciales ingresadas invalidas')

        self.context['Usuario'] = usuario
        return data
    
    def create(self,data):
        return self.context['Usuario']

class UsuarioRegisterSerializer(serializers.Serializer):

    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)
    photo = serializers.CharField()
    tipo_usuario = serializers.CharField()

    class Meta:
        model = Usuario
        fields=('email','first_name','last_name','password','photo','tipo_usuario')

    def validate(self, data):
        return data

    def create(self,data):
        data['username']=data['email']
        usuario = Usuario.objects.create_user(**data)
        return usuario
