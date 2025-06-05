from django.shortcuts import render, redirect
from .models import Eventos
from django.contrib import messages
from django.conf import settings
import os

def inicio2(request):
    listadoEventos = Eventos.objects.all()
    return render(request, "inicio2.html", {'Eventos': listadoEventos})

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
    pdfEvento=request.FILES.get("pdfEvento")

    Eventos.objects.create(nombre=nombre, descripcion=descripcion, fecha=fecha, hora=hora, logoEvento=logoEvento, pdfEvento=pdfEvento)

    #Mensaje de confirmacion 
    messages.success(request, "Evento guardado exitosamente")
    return redirect('inicio2')

# Eliminar una prueba por ID
def eliminarEvento(request, id):
    eventoEliminar = Eventos.objects.get(id=id)

    if eventoEliminar.logoEvento and os.path.isfile(os.path.join(settings.MEDIA_ROOT, eventoEliminar.logoEvento.name)):
        os.remove(os.path.join(settings.MEDIA_ROOT, eventoEliminar.logoEvento.name))

    if eventoEliminar.pdfEvento and os.path.isfile(os.path.join(settings.MEDIA_ROOT, eventoEliminar.pdfEvento.name)):
        os.remove(os.path.join(settings.MEDIA_ROOT, eventoEliminar.pdfEvento.name))

    eventoEliminar.delete()
    return redirect('inicio2')

# Mostrando formulario de ediccion
def editarEvento(request, id):
    eventoEditar = Eventos.objects.get(id=id)
    return render(request, "editarEvento.html", {'eventoEditar': eventoEditar})

def procesarEdicionEventos(request):
    
    id=request.POST["id"]
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    fecha = request.POST["fecha"]
    hora = request.POST["hora"]

    logoEvento=request.FILES.get("logoEvento")
    pdfEvento=request.FILES.get("pdfEvento")
    
    eventos2=Eventos.objects.get(id=id)
    eventos2.nombre=nombre
    eventos2.descripcion=descripcion
    eventos2.fecha=fecha
    eventos2.hora=hora

    if logoEvento :
        if eventos2.logoEvento:
            rutaLogo = os.path.join(settings.MEDIA_ROOT, str(eventos2.logoEvento))
            if os.path.isfile(rutaLogo):
                os.remove(rutaLogo)
        eventos2.logoEvento = logoEvento

    if pdfEvento:
        if eventos2.pdfEvento:
            rutaPdf = os.path.join(settings.MEDIA_ROOT, str(eventos2.pdfEvento))
            if os.path.isfile(rutaPdf):
                os.remove(rutaPdf)
        eventos2.pdfEvento = pdfEvento
        
    eventos2.save()
    #Mensaje de confirmacion
    messages.success(request, "Evento Actualizado exitosamente")
    return redirect('inicio2')