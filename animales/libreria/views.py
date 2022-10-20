from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("<h1> Bienvenido </h1>")

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def index(request):
    return render(request, 'index.html')

def peluditos(request):
    return render(request, 'peluditos.html')

def perros(request):
    return render(request, 'paginas/perros.html')

def gatos(request):
    return render(request, 'paginas/gatos.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')

def login(request):    
    return render(request, 'paginas/login.html')

def registro(request):
    return render(request, 'paginas/registro.html')