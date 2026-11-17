from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm


def inicio(request):
    return render(request, "inicio.html")


def lista_animais(request):
    animais = Animal.objects.all()
    return render(request, "lista_animais.html", {"animais": animais})


def cadastrar_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista_animais")
    else:
        form = AnimalForm()

    return render(request, "cadastrar_animal.html", {"form": form})
