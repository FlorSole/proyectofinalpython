from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def index(request):
    return render(request, 'paginas/index.html')

def peluditos(request):
    return render(request, 'peluditos.html')