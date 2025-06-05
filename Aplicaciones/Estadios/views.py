from .models import Eventos
from django.shortcuts import render, redirect
from .models import Estadios
from django.contrib import messages
from django.conf import settings
import os

def inicio(request):
    listadoEstadio = Estadios.objects.all()
    return render(request, "inicio.html", {'Estadios': listadoEstadio})

# Renderizar el formulario para nueva prueba
def nuevoEstadio(request):
    remEventos=Eventos.objects.all()
    return render(request, "nuevoEstadio.html", {'eventos':remEventos,})

# Función encargada de guardar una nueva prueba en la base de datos
def guardarEstadio(request):
    nombre = request.POST["nombre"]
    ubicacion = request.POST["ubicacion"]
    capacidad = request.POST["capacidad"]
    fecha = request.POST["fecha"]

    eventoId = request.POST["evento"]
    evento=Eventos.objects.get(id=eventoId)

    #Subiendo archivo con parentecis
    logo=request.FILES.get("logo")
    pdf=request.FILES.get("pdf")

    Estadios.objects.create(nombre=nombre, ubicacion=ubicacion, capacidad=capacidad, fecha=fecha,evento=evento, logo=logo, pdf=pdf)

    #Mensaje de confirmacion 
    messages.success(request, "Estadio guardado exitosamente")
    return redirect('inicio')

# Eliminar una prueba por ID
def eliminarEstadio(request, id):
    estadioEliminar = Estadios.objects.get(id=id)

    if estadioEliminar.logo and os.path.isfile(os.path.join(settings.MEDIA_ROOT, estadioEliminar.logo.name)):
        os.remove(os.path.join(settings.MEDIA_ROOT, estadioEliminar.logo.name))

    if estadioEliminar.pdf and os.path.isfile(os.path.join(settings.MEDIA_ROOT, estadioEliminar.pdf.name)):
        os.remove(os.path.join(settings.MEDIA_ROOT, estadioEliminar.pdf.name))

    estadioEliminar.delete()
    return redirect('inicio')

# Mostrando formulario de ediccion
def editarEstadio(request, id):
    estadioEditar = Estadios.objects.get(id=id)
    remEventos=Eventos.objects.all()
    return render(request, "editarEstadio.html", {'estadioEditar': estadioEditar, 'eventos':remEventos,})

def procesarEdicionEstadios(request):
    
    id=request.POST["id"]
    nombre = request.POST["nombre"]
    ubicacion = request.POST["ubicacion"]
    capacidad = request.POST["capacidad"]
    fecha = request.POST["fecha"]

    eventoId = request.POST["evento"]
    evento=Eventos.objects.get(id=eventoId)

    logo=request.FILES.get("logo")
    pdf=request.FILES.get("pdf")
    
    estadios2=Estadios.objects.get(id=id)
    estadios2.nombre=nombre
    estadios2.ubicacion=ubicacion
    estadios2.capacidad=capacidad
    estadios2.fecha=fecha

    estadios2.evento=evento

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