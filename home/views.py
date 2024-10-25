from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("A views index funcionou, Wow!")

def sobre(request):
    return HttpResponse("Sistema 1.0 desenvolvido por mim mesmo.")

def contato(request):
    return HttpResponse("")

def ajuda(request):
    return HttpResponse("")