from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("A views index funcionou, Wow!")

def sobre(request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvido por mim mesmo.</h1>")

def contato(request):
    return HttpResponse("Está é a página de contato.")

def ajuda(request):
    return HttpResponse("Está é a página de ajuda.")