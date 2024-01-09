from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView
)

# Create your views here.
class ReportReservaView(TemplateView):
    template_name = "reportes/reporte-reservas.html"