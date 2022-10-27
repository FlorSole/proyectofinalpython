
from django.db import models


# Create your models here.



class Usuarios(models.Model):

    nombre= models.CharField(max_length=60)
    contraseña= models.CharField(max_length=60)
    email=models.EmailField()


class animales(models.Model):

    nombre= models.CharField(max_length=60)
    tipo=models.CharField(max_length=60)
    edad=models.IntegerField()
    foto = models.ImageField(upload_to='img')
    
    
    def __str__(self):
        return self.title


