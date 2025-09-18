"""
URL configuration for Lista_de_Leitura project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name = "login"),
    path('cadastro/',views.cadastro, name="cadastro"),
    path('Cantinho_da_Leitura/',views.centro, name="centro"),
    path('ajuda/',views.ajuda, name="ajuda"),
    path('busca/',views.busca,name="busca"),
    path('minha_lista/',views.minha_lista,name="minha_lista")


]
