from django.urls import path,include
from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import * 


router = DefaultRouter()
router.register(r'experto',ExpertoViewSet,basename='experto')
router.register(r'cliente',ClienteViewSet,basename='cliente')
router.register(r'inversionista',InversionistaViewSet,basename='inversionista')
router.register(r'proyecto',ProyectoViewSet,basename='proyecto')

urlpatterns = [    
   path('',include(router.urls)) 
]