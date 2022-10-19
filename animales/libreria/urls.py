from django.urls import path
from . import views

urlpatterns =   [

    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('index', views.index, name='index'),
    path('peluditos', views.peluditos, name='peluditos'),

]