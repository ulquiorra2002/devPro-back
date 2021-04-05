from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cliente, Etapa,Experto,Inversion,Inversionista,Proyecto,Tipo
from .serializers import ProyectoSerializer,ExpertoSerializer,ExpertoUSuarioSerializer
from rest_framework import generics

from rest_framework import viewsets, mixins
# Create your views here.


class ExpertoViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Experto.objects.all()
    #serializer_class =ExpertoSerializer

    def get_serializer_class(self):
        if self.action in ('list','retrieve'):
            return ExpertoUSuarioSerializer
        return ExpertoSerializer


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

