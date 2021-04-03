from django.urls import path
from django.conf.urls import url

from . import views  
urlpatterns = [
 
    url(r'^proyecto$', views.ProyectoList.as_view()),
    url(r'^proyecto/(?P<pk>[0-9]+)$', views.ProyectoDetail.as_view()),
     url(r'^experto$', views.ExpertoList.as_view()),
    url(r'^experto/(?P<pk>[0-9]+)$', views.ExpertoDetail.as_view()),
    
    
    
]