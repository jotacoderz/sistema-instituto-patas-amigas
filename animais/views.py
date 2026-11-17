from django.shortcuts import render, redirect
from .models import Animal


def inicio(request):
    return render(request, "inicio.html")


def lista_animais(request):
    animais = Animal.objects.all()
    return render(request, "lista_animais.html", {"animais": animais})


def cadastrar_animal(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        especie = request.POST.get("especie")
        idade = request.POST.get("idade")

        Animal.objects.create(
            nome=nome,
            especie=especie,
            idade=int(idade) if idade else None
        )

        return redirect("lista_animais")

    return render(request, "cadastrar_animal.html")
