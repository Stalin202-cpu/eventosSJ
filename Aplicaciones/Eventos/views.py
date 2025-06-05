from django.shortcuts import render, redirect
from .models import Eventos
from django.contrib import messages
from django.conf import settings
import os

def inicio2(request):
    listadoEventos = Eventos.objects.all()
    return render(request, "inicio2.html", {'Evnetos': listadoEventos})

# Renderizar el formulario para nueva prueba
def nuevoEvento(request):
    return render(request, "nuevoEvento.html")

# Función encargada de guardar una nueva prueba en la base de datos
def guardarEvento(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    fecha = request.POST["fecha"]
    hora = request.POST["hora"]

    #Subiendo archivo con parentecis
    logoEvento=request.FILES.get("logoEvento")
    logoEvento=request.FILES.get("logoEvento")

    Eventos.objects.create(nombre=nombre, descripcion=descripcion, fecha=fecha, hora=hora, logoEvento=logoEvento, logoEvento=logoEvento)

    #Mensaje de confirmacion 
    messages.success(request, "Evento guardado exitosamente")
    return redirect('inicio2')

