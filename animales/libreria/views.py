from tkinter import PhotoImage
from django.shortcuts import render
from django.http import HttpResponse
from libreria.forms import registroUzu
from libreria.forms import animalform, usuarioform
from libreria.models import animales, usuario
from libreria import models

# Create your views here.

def inicio(request):
    return HttpResponse("<h1> Bienvenido </h1>")

def nosotros(request):
    return render(request, 'paginas/nosotros.html')




def usuario(request):

 if request.method == "POST":

        formulario = usuarioform(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            usuario = usuario(nombre=info["nombre"], edad=info["edad"], mail=info["email"])


            usuario.save()

            return render(request,"index")

        else:
 
            formulario = usuarioform()

        return render(request,"index", {"":formulario})


def index(request):
    return render(request, 'index.html')

def peluditos(request):
    return render(request, 'peluditos.html')

def perros(request):
    

    if request.method == "POST":

        formulario = animalform(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            perros = animales(nombre=info["nombre"],tipo=info["tipo"],edad=info["edad"])


    return render(request, 'paginas/perros.html')




def gatos(request):
    return render(request, 'paginas/gatos.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')



#Usuarios/Adoptantes- Animales - photo #


def login(request):    
    return render(request, 'paginas/login.html')

def registro(request):
    return render(request, 'paginas/registro.html')


def registroUsuario(request):


    if request.method == "POST":


        formulario = registroUzu(request.POST)

        if formulario.is_valid():

            info= formulario.cleaned_data

            u = usuario(nombre=info["nombre"],edad=info["edad"],email=info["email"])



    return render(request, 'pagina/index.html')
