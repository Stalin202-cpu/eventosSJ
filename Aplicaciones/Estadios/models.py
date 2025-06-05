from django.db import models
from Aplicaciones.Eventos.models import Eventos

# Create your models here.
class Estadios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=150)
    capacidad = models.IntegerField()
    fecha = models.DateField()
    logo=models.FileField(upload_to='cargos', null=True, blank=True)
    pdf=models.FileField(upload_to='pdf', null=True, blank=True)
    eventos = models.ForeignKey(Eventos, on_delete=models.CASCADE) 


    def __str__(self): 
        fila = "{0}:  {1}  {2}   {3} {4}"
        return fila.format(self.id, self.nombre, self.ubicacion, self.capacidad, self.fecha, self.logo, self.pdf)
