from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cliente, Etapa,Experto,Inversion,Inversionista,Proyecto,Tipo
from .serializers import ProyectoSerializer,ExpertoSerializer
from rest_framework import generics
# Create your views here.


class ExpertoList(generics.ListCreateAPIView):
    queryset = Experto.objects.all()
    serializer_class =ExpertoSerializer



class ExpertoDetail(generics.RetrieveUpdateAPIView):
    queryset = Experto.objects.all()
    serializer_class =ExpertoSerializer




class ProyectoList(generics.ListCreateAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer



class ProyectoDetail(generics.RetrieveUpdateAPIView):
    queryset = Proyecto.objects.all()
    serializer_class =ProyectoSerializer


