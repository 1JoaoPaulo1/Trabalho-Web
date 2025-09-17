from django.contrib import admin
from controle.models import Pessoa,Livro,Leitura,Logado
# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Livro)
admin.site.register(Leitura)
admin.site.register(Logado)
