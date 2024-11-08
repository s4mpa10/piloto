from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

# def base(request):
#     return render(request,'base.html')

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    return render(request,'contato.html')

def exibir_item(request, id):
    return render(request,"exibir_item.html",{'id':id})

def perfil(request,usuario):
    return render(request,"perfil.html",{'perfil':usuario})

def diasemana(request,dia):
    dia_semana = ""
    numero = 0
    if dia == 1:
        dia_semana = 'Domingo'
    elif dia == 2:
        dia_semana = 'Segunda-Feira'
    elif dia == 3:     
        dia_semana = 'Terça-Feira'
    elif dia == 4:
        dia_semana = 'Quarta-Feira'
    elif dia == 5:  
        dia_semana = 'Quinta-Feira'
    elif dia == 6:  
        dia_semana = 'Sexta-Feira'
    elif dia == 7:  
        dia_semana = 'Sábado'
    else:  
        dia_semana = 'Inválido' 
    
    return render(request, "diasemana.html", {'num':dia, 'dia':dia_semana})
    
def home_cadWeb(request):
    return render(request, "home_cadWeb.html")

    
    