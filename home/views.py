from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request,'sobre_page.html')

def entre_em_contato(request):
    return render(request,'contato_page.html')
