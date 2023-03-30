from django.shortcuts import render
from django.http import HttpResponse

def Saludar (request):
    return HttpResponse("Hola Mundo")

def Saludar_a (request , alguien):
    return HttpResponse (f"hola {alguien.title()} como estas?")

def Sumar (request, a, b):
    return HttpResponse (f"El resultado es {a+b}")