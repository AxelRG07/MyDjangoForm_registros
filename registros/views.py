from django.shortcuts import render, redirect, get_object_or_404
from .forms import EquipoForm, JugadorForm
from .models import Equipo, Jugador


# Create your views here.
def index(request):
    equipos = Equipo.objects.all()
    return render(request, 'index.html', {'equipos': equipos})

def registrar_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EquipoForm()
    return render(request, 'equipos/registrar_equipo.html', {
        'form': form,
    })

def registrar_jugador(request, id):
    equipo = get_object_or_404(Equipo, pk=id)
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_jugador = form.save(commit=False)
            nuevo_jugador.equipo = equipo
            nuevo_jugador.save()

            return redirect('equipo', id=id)
    else:
        form = JugadorForm()

    return render(request, 'jugadores/registrar_jugador.html', {
        'form': form,
        'equipo': equipo,
    })

def equipo_detalle(request, id):
    equipo = get_object_or_404(Equipo, pk=id)
    return render(request, 'equipos/equipo_detail.html', {
        'equipo': equipo,
    })

def jugador_detalle(request, id):
    jugador = get_object_or_404(Jugador, pk=id)
    return render(request, 'jugadores/jugador_detail.html', {
        'jugador': jugador,
    })