from django.shortcuts import render, redirect, get_object_or_404
from .forms import EquipoForm, JugadorForm
from .models import Equipo, Jugador
import os

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

def registrar_jugador(request, id_equipo):
    equipo = get_object_or_404(Equipo, pk=id_equipo)
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_jugador = form.save(commit=False)
            nuevo_jugador.equipo = equipo
            nuevo_jugador.save()

            return redirect('equipo', id_equipo=id_equipo)
    else:
        form = JugadorForm()

    return render(request, 'jugadores/registrar_jugador.html', {
        'form': form,
        'equipo': equipo,
    })

def equipo_detalle(request, id_equipo):
    equipo = get_object_or_404(Equipo, pk=id_equipo)
    return render(request, 'equipos/equipo_detail.html', {
        'equipo': equipo,
    })

def jugador_detalle(request, id_jugador):
    jugador = get_object_or_404(Jugador, pk=id_jugador)
    return render(request, 'jugadores/jugador_detail.html', {
        'jugador': jugador,
    })

def eliminar_jugador(request, id_jugador):
    jugador = get_object_or_404(Jugador, pk=id_jugador)
    if request.method == 'POST':
        id_equipo = jugador.equipo.id
        jugador.delete()
        return redirect('equipo', id_equipo=id_equipo)

    else:
        return render(request, 'jugadores/eliminar_jugador.html', {
            'jugador': jugador,
        })

def actualizar_jugador(request, id_jugador):
    jugador = get_object_or_404(Jugador, pk=id_jugador)
    foto_path = jugador.foto.path if jugador.foto.path else None
    pdf_path = jugador.identificacion_pdf.path if jugador.identificacion_pdf.path else None

    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES, instance=jugador)
        if form.is_valid():
            if 'foto' in request.FILES and foto_path:
                if os.path.exists(foto_path):
                    os.remove(foto_path)

            if 'identificacion_pdf' in request.FILES and pdf_path:
                if os.path.exists(pdf_path):
                    os.remove(pdf_path)

            form.save()
            return redirect('jugador', id_jugador=id_jugador)
    else:
        form = JugadorForm(instance=jugador)
    return render(request, 'jugadores/registrar_jugador.html', {
        'form': form,
        'jugador': jugador,
    })