
from tabnanny import verbose
from django.db import models


# Create your models here.



class Usuarios(models.Model):

    nombre= models.CharField(max_length=60)
    contraseña= models.CharField(max_length=60)
    email=models.EmailField()


class Perritos(models.Model):

    nombre= models.CharField(max_length=60)
    raza=models.CharField(max_length=60)
    edad=models.IntegerField()
    fotoperri = models.ImageField(upload_to = 'libreria/static/assets/img', verbose_name = 'Perri', null=True)
    
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad} - Raza: {self.raza} - Foto: {self.foto}"


class Gatitos(models.Model):

    nombre= models.CharField(max_length=60)
    raza=models.CharField(max_length=60)
    edad=models.IntegerField()
    fotogati = models.ImageField(upload_to = 'libreria/static/assets/img', verbose_name = 'Gati', null=True)
    
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad} - Raza: {self.raza} - Foto: {self.foto}"