from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


from rest_framework.routers import DefaultRouter

from .viewsets import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuario',UsuarioViewSet,basename='usuario')

urlpatterns = [
    path('',include(router.urls)),
    
]