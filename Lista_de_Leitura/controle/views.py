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
     return redirect("centro")
    else:
     l = Logado(pessoa = p,logado = False)
     l.save()
     p = Pessoa.objects.get(matricula = valores["matricula"],senha = valores["senha"])
     online = Logado.objects.get(pessoa = p)
     online.logado = True
     online.save()     
     return redirect("centro")
     
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


def centro(request):
 logado = Logado.objects.filter(logado=True)
 if len(logado) == 1:
  return render(request,"sites/Cantinho da Leitura.html")
 else:
  logado = Logado.objects.all()
  for i in logado:
   i.logado = False
   i.save()
  return render(request,"sites/Login.html")  

def ajuda(request):
 logado = Logado.objects.filter(logado=True)
 if len(logado) == 1:
  return render(request,"sites/Ajuda.html")
 else:
  logado = Logado.objects.all()
  for i in logado:
   i.logado = False
   i.save()
  return render(request,"sites/Login.html")


def busca(request):
 logado = Logado.objects.filter(logado=True)
 if len(logado) == 1:
  logado = Logado.objects.get(logado=True)
  livro = Livro.objects.all()
  return render(request,"sites/Busca.html",{"livro":livro})
  
 else:
  logado = Logado.objects.all()
  for i in logado:
   i.logado = False
   i.save()
  return render(request,"sites/Login.html")


def minha_lista(request):
 logado = Logado.objects.filter(logado=True)
 if len(logado) == 1:
  if request.method == "GET":
   logado = Logado.objects.get(logado=True)
   leitura = Leitura.objects.filter(pessoa = logado.pessoa)
  

   return render(request,"sites/Minha Lista.html",{"leitura":leitura})
  else:
   if request.method =="POST":
    valores = (request.POST)
    leitura = Leitura.objects.get(id_leitura=valores["identificar"])
    livro = Livro.objects.get(id_livro = leitura.livro.id_livro)
    if int(valores["pagina_atual"]) >= 0 and int(valores["pagina_atual"]) <= livro.numero_paginas:
     leitura.pagina_atual = valores["pagina_atual"]
     leitura.save()
     logado = Logado.objects.get(logado=True)
     leitura = Leitura.objects.filter(pessoa = logado.pessoa)
     return render(request,"sites/Minha Lista.html",{"leitura":leitura})
    else:
     logado = Logado.objects.filter(logado=True)
     if len(logado) == 1:
      if request.method == "GET":
       logado = Logado.objects.get(logado=True)
       leitura = Leitura.objects.filter(pessoa = logado.pessoa)
       return render(request,"sites/Minha Lista.html",{"leitura":leitura})
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

