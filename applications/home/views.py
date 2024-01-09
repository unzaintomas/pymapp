from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from applications.reserva.models import Reserva
from django.db.models import Count, Sum


# Create your views here.
@login_required
def dashboard_view(request):
    # Obtener el número de reservas no canceladas
    reservas_no_canceladas = Reserva.objects.filter(cancelada=False).count()

    # Obtener el total recaudado de reservas pagadas
    recaudado = Reserva.objects.filter(pagado=True).aggregate(Sum('precio'))['precio__sum'] or 0

    # Formatear el total recaudado con separador de miles y sin decimales
    recaudado_formateado = "{:,.0f}".format(recaudado)

    context = {
        'reservas_no_canceladas': reservas_no_canceladas,
        'recaudado': recaudado_formateado,
    }

    return render(request, "home/dashboard.html", context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login exitoso.')
            return redirect('home_app:dashboard')  # Cambia 'dashboard' por la URL a la que quieres redirigir después del login.
        else:
            messages.error(request, 'Credenciales inválidas.')
    
    return render(request, 'registration/login.html')


def user_logout(request):
    logout(request)
    return redirect('home_app:dashboard') 
