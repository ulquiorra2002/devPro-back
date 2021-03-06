from rest_framework import serializers
#from rest_framework_jwt.settings import api_settings
#from django.contrib.auth.models import User
from .models import *
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer



class ExpertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experto
        fields = ('id','usuario', 'id_tipo',
                  'codigo_experto', 'descripcion_experto')

class ExpertoUSuarioSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    class Meta:
        model = Experto
        fields = ('id','usuario', 'id_tipo',
                  'codigo_experto', 'descripcion_experto')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ClienteUSuarioSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    class Meta:
        model = Cliente
        fields = '__all__'


class InversionistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inversionista
        fields = '__all__'

class InversionistaUSuarioSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    class Meta:
        model = Inversionista
        fields = '__all__'


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class ProyectoClienteSerializer(serializers.ModelSerializer):
    id_cliente=ClienteUSuarioSerializer(read_only=True)
    class Meta:
        model = Proyecto
        fields = '__all__'



