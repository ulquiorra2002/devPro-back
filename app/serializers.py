from rest_framework import serializers
#from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from app.models import Cliente, Etapa,Experto,Inversion,Inversionista,Persona,Proyecto,Tipo




class ExpertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experto
        fields = ('id_experto', 'id_persona', 'id_tipo',
                  'codigo_experto', 'descripcion_experto')






class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('id_proyecto', 'id_etapa', 'id_inversion',
                  'nombre_proyecto', 'descripcion_proyecto', 'financiamiento_proyecto')






class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id_persona', 'numero_documento_persona','direccion_persona','usuario')