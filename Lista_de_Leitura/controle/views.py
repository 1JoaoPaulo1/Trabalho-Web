from django.shortcuts import render,redirect
from .models import Pessoa,Livro,Leitura,Nota,Logado

# Create your views here.
def login(request):
 if request.method=="POST":
  logado = Logado.objects.all()
  for i in logado:
   i.logado = False
   i.save()
  valores = (request.POST)
  if len(valores["matricula"]) == 10 and  len(valores["senha"]) == 3:
   p = Pessoa.objects.filter(matricula = valores["matricula"],senha = valores["senha"])
   if len(p) == 1:
    p = Pessoa.objects.get(matricula = valores["matricula"],senha = valores["senha"])
    if len(Logado.objects.filter(pessoa = p)) == 1:
     online = Logado.objects.get(pessoa = p)
     online.logado = True
     online.save()
     return render(request,"sites/Login.html")
    else:
     l = Logado(pessoa = p,logado = False)
     l.save()
     p = Pessoa.objects.get(matricula = valores["matricula"],senha = valores["senha"])
     online = Logado.objects.get(pessoa = p)
     online.logado = True
     online.save()     
     return render(request,"sites/Login.html")

     
   else:
    return render(request,"sites/Login.html")

  else:
   logado = Logado.objects.all()
   for i in logado:
    i.logado = False
    i.save()
   return render(request,"sites/Login.html")

 else:
  logado = Logado.objects.all()
  for i in logado:
   i.logado = False
   i.save()
  return render(request,"sites/Login.html")

def cadastro(request):
 if request.method=="POST":
  pass
 else:
  return render(request,"sites/Cadastro.html")

 
