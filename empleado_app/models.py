from django.db import models

from .validators import validar_solo_letras
from .validators import validar_dominio_correo
# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return (f'{self.nombre}')


class Empleado(models.Model):
    nombre = models.CharField(max_length=30, validators= [validar_solo_letras])
    apellido = models.CharField(max_length=30, validators= [validar_solo_letras])
    correo = models.EmailField(unique=True, validators=[validar_dominio_correo])  # Correo único
    #departamento =  Sirve para relacionar el empleado con el departamento
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE) 

    def __str__(self):
        return (f'{self.nombre}, {self.apellido}')

    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=300)

    def __str__(self):
        return (f'{self.nombre}')


class Asignacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField() #Para hora y fecha seria DateTime

    def __str__(self):
        return (f'{self.empleado}, {self.proyecto}')
    







