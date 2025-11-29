from django.shortcuts import render
from django.http import HttpResponse

def pruebas(request):
    return HttpResponse("Bienvenido a Django desde unitecnar")

def template_view(request):
    return render(request, 'index.html')
