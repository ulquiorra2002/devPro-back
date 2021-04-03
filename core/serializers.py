from rest_framework import serializers
#from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import Cliente, Etapa,Experto,Inversion,Inversionista,Proyecto,Tipo




class ExpertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experto
        fields = ('usuario', 'id_tipo',
                  'codigo_experto', 'descripcion_experto')






class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('id_etapa', 'id_inversion',
                  'nombre_proyecto', 'descripcion_proyecto', 'financiamiento_proyecto')



