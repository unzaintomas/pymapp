#
from django.urls import path
from . import views

app_name = "reportes_app"

urlpatterns = [
    path(
        'reportes/', 
        views.ReportReservaView.as_view(),
        name='reporte-reservas',
    )
]