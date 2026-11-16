from django.shortcuts import render
from .models import Animal


def inicio(request):
    return render(request, "inicio.html")


def lista_animais(request):
    animais = Animal.objects.all()
    return render(request, "lista_animais.html", {"animais": animais})


def cadastrar_animal(request):
    return render(request, "cadastrar_animal.html")
