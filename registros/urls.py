from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('equipo/add/', registrar_equipo, name='registrar_equipo'),
    path('equipo/<int:id_equipo>/', equipo_detalle, name='equipo'),
    path('equipo/<int:id>/registrar-jugador', registrar_jugador, name='registrar_jugador'),
    path('jugador/<int:id_jugador>/', jugador_detalle, name='jugador'),
    path('jugador/<int:id_jugador>/eliminar', eliminar_jugador, name='eliminar_jugador'),
]