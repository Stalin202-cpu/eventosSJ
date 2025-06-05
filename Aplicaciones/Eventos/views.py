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
def editarEstadio(request, id):
    estadioEditar = Estadios.objects.get(id=id)
    return render(request, "editarEstadio.html", {'estadioEditar': estadioEditar})

def procesarEdicionEstadios(request):
    
    id=request.POST["id"]
    nombre = request.POST["nombre"]
    ubicacion = request.POST["ubicacion"]
    capacidad = request.POST["capacidad"]
    fecha = request.POST["fecha"]

    logo=request.FILES.get("logo")
    pdf=request.FILES.get("pdf")
    
    estadios2=Estadios.objects.get(id=id)
    estadios2.nombre=nombre
    estadios2.ubicacion=ubicacion
    estadios2.capacidad=capacidad
    estadios2.fecha=fecha

    if logo :
        if estadios2.logo:
            rutaLogo = os.path.join(settings.MEDIA_ROOT, str(estadios2.logo))
            if os.path.isfile(rutaLogo):
                os.remove(rutaLogo)
        estadios2.logo = logo

    if pdf:
        if estadios2.pdf:
            rutaPdf = os.path.join(settings.MEDIA_ROOT, str(estadios2.pdf))
            if os.path.isfile(rutaPdf):
                os.remove(rutaPdf)
        estadios2.pdf = pdf
        
    estadios2.save()
    #Mensaje de confirmacion
    messages.success(request, "Estadio Actualizado exitosamente")
    return redirect('inicio')