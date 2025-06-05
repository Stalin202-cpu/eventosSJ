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
    return render(request, "nuevoEstadio.html")

# Función encargada de guardar una nueva prueba en la base de datos
def guardarEstadio(request):
    nombre = request.POST["nombre"]
    ubicacion = request.POST["ubicacion"]
    capacidad = request.POST["capacidad"]
    fecha = request.POST["fecha"]

    #Subiendo archivo con parentecis
    logo=request.FILES.get("logo")
    pdf=request.FILES.get("pdf")

    Estadios.objects.create(nombre=nombre, ubicacion=ubicacion, capacidad=capacidad, fecha=fecha, logo=logo, pdf=pdf)

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
    return render(request, "editarEstadio.html", {'cajeroEditar': estadioEditar})

def procesarEdicionCajeros(request):
    
    id=request.POST["id"]
    nombre = request.POST["nombre"]
    cedula = request.POST["cedula"]
    turno = request.POST["turno"]
    logo=request.FILES.get("logo")
    pdf=request.FILES.get("pdf")
    
    cajeros2=Cajeros.objects.get(id=id)
    cajeros2.nombre=nombre
    cajeros2.cedula=cedula
    cajeros2.turno=turno
    if logo :
        if cajeros2.logo:
            rutaLogo = os.path.join(settings.MEDIA_ROOT, str(cajeros2.logo))
            if os.path.isfile(rutaLogo):
                os.remove(rutaLogo)
        cajeros2.logo = logo

    if pdf:
        if cajeros2.pdf:
            rutaPdf = os.path.join(settings.MEDIA_ROOT, str(cajeros2.pdf))
            if os.path.isfile(rutaPdf):
                os.remove(rutaPdf)
        cajeros2.pdf = pdf
        
    cajeros2.save()
    #Mensaje de confirmacion
    messages.success(request, "Cajero Actualizado exitosamente")
    return redirect('inicio')