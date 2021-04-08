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


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

