from django.db import models
from django.conf import settings
from django.utils import timezone
from macaddress.fields import MACAddressField
#from macaddress.fields import MACAddressField



# Create your models here.

#  Creacion de modelo para aplicacion de conexion de Redes

class Perfil(models.Model):
    #tipo de datos 
    nombre = models.CharField(max_length=50)
    ci = models.CharField(max_length=10)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    fecha = models.DateField()


#Class Grupo(models.Model):

class Direccion(models.Model):
  
    DireccionIP = models.GenericIPAddressField(db_index=True, null=True, verbose_name='IP Address',unique=True)
    puerta_enlace=models.GenericIPAddressField()
    Mascara=models.GenericIPAddressField()
    #Permisos= models.CharField(max_length=50)
   # grupo= models.ForeignKey(Grupo, max_length=50)
    #equipo=models.ManyToManyField(Equipo)



class Equipo(models.Model):
    NombreHost=models.CharField(max_length=50)
    SistemaOperativo= models.CharField(max_length=50)
    MAC=MACAddressField(blank=True, integer=False)
    MAC1=models.CharField(max_length=50)
    #Adaptador=models.CharField(max_length=50)
    direccion=models.ManyToManyField(Direccion, null=True, blank=True, through='Relacion', on_delete=models.CASCADE)
    #perfil1=models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.CASCADE)


class Relacion(models.Model):
    direccion = models.ForeignKey(Direccion, null=True, blank=True, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, null=True, blank=True, on_delete=models.CASCADE)
    FechaInicio=models.DateField()
    FechaFinal=models.DateField()
    





