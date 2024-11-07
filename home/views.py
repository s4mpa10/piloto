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
    if dia == 1:
        return render(request, "diasemana.html", {'num':dia, 'dia':'Domingo'})
    elif dia == 2:
        return render(request, "diasemana.html", {'num':dia, 'dia':'Segunda-Feira'})
    elif dia == 3:     
        return render(request, "diasemana.html", {'num':dia, 'dia':'Terça-Feira'})
    elif dia == 4:
        return render(request, "diasemana.html", {'num':dia, 'dia':'Quarta-Feira'})
    elif dia == 5:  
        return render(request, "diasemana.html", {'num':dia, 'dia':'Quinta-Feira'})
    elif dia == 6:  
        return render(request, "diasemana.html", {'num':dia, 'dia':'Sexta-Feira'})
    elif dia == 7:  
        return render(request, "diasemana.html", {'num':dia, 'dia':'Sábado'})
    else:  
        return render(request, "diasemana.html", {'num':dia, 'dia':'Error 900: Dia inválido.'})    
    
def home_cadWeb(request):
    return render(request, "home_cadWeb.html")
    
    
    