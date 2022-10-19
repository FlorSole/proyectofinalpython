from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns =   [

    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('index', views.index, name='index'),
    path('peluditos', views.peluditos, name='peluditos'),
    path('usuarios/', views.index, name='usuarios.urls'),
    path('perros', views.perros, name='perros.urls'),
    path('gatos', views.gatos, name='gatos.urls'),
    path('contacto', views.contacto, name='contacto.urls'),

]