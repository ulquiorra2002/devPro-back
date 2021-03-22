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
        Usuario = authenticate(
            username=data['email'], password=data['password'])
        if not Usuario:
            raise serializers.ValidationError('Credenciales ingresadas invalidas')

        self.context['Usuario'] = Usuario
        return data
    
    def create(self,data):
        return self.context['Usuario']

class UsuarioRegisterSerializer(serializers.Serializer):

    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = Usuario
        fields=['email','first_name','last_name']

    def create(self,data):
        Usuario = Usuario.objects.create(**data)
        return Usuario
