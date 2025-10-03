from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('equipo/add/', registrar_equipo, name='registrar_equipo'),
    path('equipo/<int:id>/', equipo_detalle, name='equipo'),
]