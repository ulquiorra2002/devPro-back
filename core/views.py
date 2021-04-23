from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework import viewsets, mixins
# Create your views here.


class ExpertoViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Experto.objects.all()

    def get_serializer_class(self):
        if self.action in ('list','retrieve'):
            return ExpertoUSuarioSerializer
        return ExpertoSerializer

class ClienteViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Cliente.objects.all()

    def get_serializer_class(self):
        if self.action in ('list','retrieve'):
            return ClienteUSuarioSerializer
        return ClienteSerializer

class InversionistaViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Inversionista.objects.all()

    def get_serializer_class(self):
        if self.action in ('list','retrieve'):
            return InversionistaUSuarioSerializer
        return InversionistaSerializer


class ProyectoViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Proyecto.objects.all()

    def get_serializer_class(self):
        if self.action in ('list','retrieve'):
            return ProyectoClienteSerializer
        return ProyectoSerializer

    @action(detail=False,methods=['get'],url_path='cliente/(?P<id>[^/.]+)')
    def cliente(self,request,id,pk=None):
        id=int(id)
        print(id)
        proyectos = Proyecto.objects.filter(id_cliente__id=id)
        data = ProyectoSerializer(proyectos,many=True).data

        return Response(data)



