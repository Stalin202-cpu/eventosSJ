from django.db import models

# Create your models here.
class Estadios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=150)
    capacidad = models.IntegerField()
    fecha = models.DateField()

    def __str__(self): 
        fila = "{0}:  {1}  {2}   {3} {4}"
        return fila.format(self.id, self.nombre, self.ubicacion, self.capacidad, self.fecha)
