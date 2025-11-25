from django.db import models

# Create your models here.

class Pessoa(models.Model):
 id_pessoa = models.AutoField(primary_key=True)
 matricula = models.CharField(max_length=10,unique=True)
 senha = models.CharField(max_length=5)
 curso = models.CharField(max_length=30)
 def __str__(p):
  return f"{p.matricula}: {p.curso}"

class Livro(models.Model):
 id_livro = models.AutoField(primary_key=True)
 nome_livro = models.CharField(max_length=250)
 nome_autor = models.CharField(max_length=250)
 codigo_livro = models.CharField(max_length=80, unique=True)

 def __str__(l):
  return f"{l.nome_livro}"

class Leitura(models.Model):
 id_leitura = models.AutoField(primary_key=True)
 livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
 pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
 pagina_atual = models.IntegerField()
 nota = models.IntegerField(choices=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)])
 def __str__(L):
  return f"Leitura de {L.pessoa.matricula} do Livro: {L.livro.nome_livro}"

class Logado(models.Model):
 id_login = models.AutoField(primary_key=True)
 pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,unique=True)
 logado = models.BooleanField(choices=[(True,"sim"),(False,"não")])
 def __str__(Log):
  return f"Matrícula: {Log.pessoa.matricula}. Estado de  login: {Log.logado}"
 
