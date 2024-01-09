# reservas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Reserva
from .forms import ReservaForm
from datetime import datetime
from django.http import JsonResponse
from copy import deepcopy

@login_required
def reservas_json(request):
    reservas = Reserva.objects.filter(cancelada=False)

    eventos = []
    for reserva in reservas:
        title = f" - {reserva.fecha_fin.strftime('%H:%M')} {reserva.cliente.nombre}"
        eventos.append({
            'title': title,
            'start': reserva.fecha_inicio.strftime('%Y-%m-%dT%H:%M:%S'),  # Formato ISO 8601
            'end': reserva.fecha_fin.strftime('%Y-%m-%dT%H:%M:%S'),  # Formato ISO 8601
            'display': title  # Especifica el texto que se mostrará en el evento
        })

    return JsonResponse(eventos, safe=False)


@login_required
def reserva_list(request):
    reservas = Reserva.objects.filter(cancelada=False)
    return render(request, 'reservas/reservas.html', {'reservas': reservas})


@login_required
def reserva_create(request):
    if request.method == 'POST':
        # Crear una copia modificable del objeto QueryDict
        mutable_post_data = deepcopy(request.POST)

        # Modificar la copia según sea necesario
        fecha_inicio_str = mutable_post_data.get('fecha_inicio', '')
        fecha_fin_str = mutable_post_data.get('fecha_fin', '')

        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, '%m/%d/%Y %I:%M %p')
            fecha_fin = datetime.strptime(fecha_fin_str, '%m/%d/%Y %I:%M %p')
        except ValueError:
            return JsonResponse({'status': 'error', 'errors': 'Formato de fecha y hora no válido'})

        mutable_post_data['fecha_inicio'] = fecha_inicio
        mutable_post_data['fecha_fin'] = fecha_fin

        # Asignar automáticamente el operador logueado al campo 'operador' del formulario
        mutable_post_data['operador'] = request.user.id

        # Crear un nuevo formulario con la copia modificada
        form = ReservaForm(mutable_post_data)

        if form.is_valid():
            #form.save()
            #return redirect('reserva_app:reserva_list')
            reserva = form.save()
            return JsonResponse({'status': 'success', 'message': 'Reserva creada exitosamente'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = ReservaForm()
    return render(request, 'reservas/reserva_new_form.html', {'form': form})


@login_required
def reserva_edit(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)

    if request.method == 'POST':
        # Crear una copia modificable del objeto QueryDict
        mutable_post_data = deepcopy(request.POST)

        # Modificar la copia según sea necesario
        fecha_inicio_str = mutable_post_data.get('fecha_inicio', '')
        fecha_fin_str = mutable_post_data.get('fecha_fin', '')

        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, '%m/%d/%Y %I:%M %p')
            fecha_fin = datetime.strptime(fecha_fin_str, '%m/%d/%Y %I:%M %p')
        except ValueError:
            return JsonResponse({'status': 'error', 'errors': 'Formato de fecha y hora no válido'})

        mutable_post_data['fecha_inicio'] = fecha_inicio
        mutable_post_data['fecha_fin'] = fecha_fin

        # Crear un nuevo formulario con la copia modificada
        form = ReservaForm(mutable_post_data, instance=reserva)
        #form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            #form.save()
            #return redirect('reserva_app:reserva_list')
            reserva = form.save()
            return JsonResponse({'status': 'success', 'message': 'Reserva actualizada exitosamente'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'reservas/reserva_edit_form.html', {'form': form, 'reserva': reserva})


@login_required
def reserva_delete(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)

    if request.method == 'POST':
        # Actualizar el campo 'cancelada' en lugar de eliminar físicamente
        reserva.cancelada = True  
        reserva.save()
        return JsonResponse({'status': 'success', 'message': 'Reserva cancelada exitosamente'})

    return render(request, 'reservas/reserva_delete_form.html', {'reserva': reserva})
