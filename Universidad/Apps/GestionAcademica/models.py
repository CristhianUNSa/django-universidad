from django.db import models

# Create your models here.

class Alumno(models.Model):
    Apellido = models.CharField(max_length=35)
    Nombre = models.CharField(max_length=35)
    DNI = models.CharField(max_length=8)
    FechaNacimiento = models.DateField()
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')

    def NombreCompleto(self):
        cadena = "{0}, {1}"
        return cadena.format(self.Apellido, self.Nombre)

    def __str__(self):
        return self.NombreCompleto()

