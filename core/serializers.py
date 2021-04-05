from rest_framework import serializers
#from rest_framework_jwt.settings import api_settings
#from django.contrib.auth.models import User
from .models import Cliente, Etapa,Experto,Inversion,Inversionista,Proyecto,Tipo

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





class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('id', 'id_inversion',
                  'nombre_proyecto', 'descripcion_proyecto', 'financiamiento_proyecto')



