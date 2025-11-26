from django.shortcuts import render,redirect
from .models import Pessoa,Livro,Leitura,Logado

# Create your views here.
def login(request):
 if request.method=="POST":
  logado = Logado.objects.all()
  for i in logado:
   i.logado = False
   i.save()
  valores = (request.POST)
  if len(valores["matricula"]) == 10 and  len(valores["senha"]) == 5:
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
  valores = request.POST
  if len(Pessoa.objects.filter(matricula=valores["matricula"])) == 0 and len(valores["senha"]) == 5:
   p = Pessoa(matricula=valores["matricula"], senha=valores["senha"],curso=valores["dropdown"])
   p.save()
   return redirect("login")
  else:
   return render(request,"sites/Cadastro.html")
   
 else:
  return render(request,"sites/Cadastro.html")


def centro(request):
 if request.method =="POST":
  logado = Logado.objects.all()
  for i in logado:
   i.logado = False
   i.save()
  return redirect(login)
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
 if request.method =="POST":
  logado = Logado.objects.all()
  for i in logado:
   i.logado = False
   i.save()
  return redirect(login)
 
 logado = Logado.objects.filter(logado=True)
 if len(logado) == 1:
  return render(request,"sites/Ajuda.html")
 else:
  logado = Logado.objects.all()
  for i in logado:
   i.logado = False
   i.save()
  return redirect(login)


def busca(request):
 logado = Logado.objects.filter(logado=True)
 if len(logado) == 1:
  logado = Logado.objects.get(logado=True)
  livro = Livro.objects.all()
  leitura = Leitura.objects.filter(pessoa = logado.pessoa).order_by("id_leitura")
  for i in leitura:
   livro = livro.exclude(id_livro = i.livro.id_livro)

  if request.method =="POST":
   valor = (request.POST)
   if valor["identificar"] =="SISTEMALOGOFF":
    logado = Logado.objects.all()
    for i in logado:
     i.logado = False
     i.save()
    return redirect(login)
   if valor["tipo"] == "busca":
    logado = Logado.objects.get(logado=True)
    livro = Livro.objects.filter(nome_livro__contains=valor["identificar"])
    leitura = Leitura.objects.filter(pessoa = logado.pessoa).order_by("id_leitura")
    for i in leitura:
     livro = livro.exclude(id_livro = i.livro.id_livro)
    return render(request,"sites/Busca.html",{"livro":livro})
   if valor["tipo"] == "adicionar":
    logado = Logado.objects.get(logado=True) 
    if len(Leitura.objects.filter(pessoa = logado.pessoa,livro=valor["identificar"])) == 0:
     p = Pessoa.objects.get(id_pessoa = logado.pessoa.id_pessoa)
     liv = Livro.objects.get(id_livro = valor["identificar"])
     l = Leitura(livro = liv,pessoa = p,pagina_atual = 1,nota=0)
     l.save()
     livro = Livro.objects.all()
     leitura = Leitura.objects.filter(pessoa = logado.pessoa).order_by("id_leitura")
     for i in leitura:
      livro = livro.exclude(id_livro = i.livro.id_livro)
     return redirect("minha_lista")
    else:
     logado = Logado.objects.get(logado=True)
     livro = Livro.objects.all()
     leitura = Leitura.objects.filter(pessoa = logado.pessoa).order_by("id_leitura")
     for i in leitura:
      livro = livro.exclude(id_livro = i.livro.id_livro)
     return render(request,"sites/Busca.html",{"livro":livro})        

    
  else:
   livro = Livro.objects.all()
   leitura = Leitura.objects.filter(pessoa = logado.pessoa).order_by("id_leitura")
   for i in leitura:
    livro = livro.exclude(id_livro = i.livro.id_livro)
   return render(request,"sites/Busca.html",{"livro":livro})

 else:
  logado = Logado.objects.all()
  for i in logado:
   i.logado = False
   i.save()
   return redirect("login")







def minha_lista(request):
 logado = Logado.objects.filter(logado=True)
 if len(logado) == 1:
  if request.method == "GET":
   logado = Logado.objects.get(logado=True)
   leitura = Leitura.objects.filter(pessoa = logado.pessoa).order_by("id_leitura")
   leitura = leitura[::-1]
  
   return render(request,"sites/Meus Livros.html",{"leitura":leitura})
  
  elif request.method=="POST" and request.POST["identificar"] == "remover":
    a = Leitura.objects.get(id_leitura =int(request.POST["remover"]))
    a.delete()
    logado = Logado.objects.get(logado=True)
    leitura = Leitura.objects.filter(pessoa = logado.pessoa).order_by("id_leitura")
    return render(request,"sites/Meus Livros.html",{"leitura":leitura})

  elif request.method=="POST" and request.POST["identificar"] == "SISTEMALOGOFF":
   logado = Logado.objects.all()
   for i in logado:
    i.logado = False
    i.save()
   return redirect(login)

  elif request.method=="POST" and request.POST["identificar"] == "GERARPDF":
   logado = Logado.objects.get(logado=True)
   leitura = Leitura.objects.filter(pessoa = logado.pessoa).order_by("id_leitura")
   leitura = leitura[::-1]
   x = open("Meus_Livros.txt","w",encoding="utf8")
   x.write("")
   x.close()
   x = open("Meus_Livros.txt","a",encoding="utf8")
   for i in leitura:
    x.write(f"TÍTULO: {i.livro.nome_livro}\n")
    x.write(f"Código: {i.livro.codigo_livro}\n")
    x.write(f"Autor(es): {i.livro.nome_autor}\n")
    x.write(f"Página Atual: {i.pagina_atual}\n")
    x.write(f"Nota: {i.nota} estrelas\n")
    x.write("\n")
   x.close()
   return render(request,"sites/Meus Livros.html",{"leitura":leitura})

    
  else:
   if request.method =="POST":
    valores = (request.POST)
    leitura = Leitura.objects.get(id_leitura=valores["identificar"])
    livro = Livro.objects.get(id_livro = leitura.livro.id_livro)
    if int(valores["pagina_atual"]) >= 0 and int(valores["pagina_atual"]) <= 9999 and int(valores["nota"])>= 0 and int(valores["nota"])<=5:
     leitura.pagina_atual = valores["pagina_atual"]
     leitura.save()
     Ler = Leitura.objects.get(id_leitura=valores["identificar"])
     Ler.nota = int(valores["nota"])
     Ler.save()
     logado = Logado.objects.get(logado=True)
     leitura = Leitura.objects.filter(pessoa = logado.pessoa).order_by("id_leitura")
     return render(request,"sites/Meus Livros.html",{"leitura":leitura})
    
    else:
     logado = Logado.objects.filter(logado=True)
     if len(logado) == 1:
      if request.method == "GET":
       logado = Logado.objects.get(logado=True)
       leitura = Leitura.objects.filter(pessoa = logado.pessoa).order_by("id_leitura")
  
       return render(request,"sites/Meus Livros.html",{"leitura":leitura})
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
   return redirect("login")

