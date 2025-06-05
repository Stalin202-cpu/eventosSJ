from django.shortcuts import render
from .models import Estadios

# Create your views here.
def inicio(request):
    listadoEstadio = Estadios.objects.all()
    return render(request, "inicio.html", {'Estadios': listadoEstadio})
