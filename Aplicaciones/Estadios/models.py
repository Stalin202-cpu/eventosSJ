from django.db import models

# Create your models here.
class Estadios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=150)
    capacidad = models.IntegerField()
    fecha_inauguracion = models.DateField()
