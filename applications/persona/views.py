# persona/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Cliente
from applications.reserva.models import Reserva
from .forms import ClienteForm  


@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    form = ClienteForm()
    return render(request, 'persona/clientes.html', {'clientes': clientes, 'form':form})


@login_required
def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    reservas = Reserva.objects.filter(cliente=cliente)

    # Serializar las reservas en formato JSON
    reservas_data = [{'fecha_inicio': reserva.fecha_inicio.strftime('%d/%m/%Y %H:%M:%S'),
        'fecha_fin': reserva.fecha_fin.strftime('%d/%m/%Y %H:%M:%S')} for reserva in reservas]

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'cliente': {'id': cliente.id, 'nombre': cliente.nombre, 'celular': cliente.celular, 'email': cliente.email}, 'reservas': reservas_data})
    else:
        return render(request, 'persona/cliente_detail.html', {'cliente': cliente, 'reservas': reservas})


@login_required
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            #form.save()
            #return redirect('persona_app:cliente_list')
            cliente = form.save()
            cliente_data = {
                'id': cliente.id,
                'nombre': cliente.nombre,
                'celular': cliente.celular,
                'email': cliente.email
            }
            return JsonResponse({'status': 'success', 'message': 'Cliente registrado exitosamente', 'cliente': cliente_data})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = ClienteForm()
    return render(request, 'persona/cliente_new_form.html', {'form': form})


@login_required
def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            #form.save()
            #return redirect('persona_app:cliente_list')
            cliente = form.save()
            # Devolver información del nuevo cliente en formato JSON
            
            return JsonResponse({'status': 'success', 'message': 'Cliente actualizado exitosamente'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'persona/cliente_edit_form.html', {'form': form, 'cliente': cliente})


@login_required
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        cliente.delete()
        #return redirect('persona_app:cliente_list')
        return JsonResponse({'status': 'success', 'message': 'Cliente eliminado exitosamente'})

    return render(request, 'persona/cliente_delete_form.html', {'cliente': cliente})
