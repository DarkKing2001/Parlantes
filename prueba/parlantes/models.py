from django.db import models

# Create your models here.

class Parlante(models.Model):
    id_parlante      = models.AutoField(db_column='id_alumno', primary_key=True)
    nombre           = models.CharField(max_length=20, blank=True, null=True)
    tipo             = models.CharField(max_length=10, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)

    #toString
    def __str__(self):
        return  self.nombre+", "+self.tipo+", " + self.foto.__str__()

    class Meta:
        ordering = ["tipo"]