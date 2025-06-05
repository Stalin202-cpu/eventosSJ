from django.db import models

# Create your models here.
class Eventos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField()
    fecha = models.DateField()
    hora = models.TimeField()
    logoEvento=models.FileField(upload_to='cargos', null=True, blank=True)
    pdfEvento=models.FileField(upload_to='pdf', null=True, blank=True)
    def __str__(self): 
        fila = "{0}:  {1}  {2}   {3} {4} {5} {6}"
        return fila.format(self.id, self.nombre, self.descripcion, self.fecha, self.hora, self.logoEvento, self.pdfEvento)


