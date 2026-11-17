from django.test import TestCase
from django.urls import reverse
from .models import Animal


class AnimalTestCase(TestCase):

    def test_cadastrar_animal(self):
        animal = Animal.objects.create(
            nome="Mel",
            especie="Cachorro",
            idade=3
        )

        self.assertEqual(animal.nome, "Mel")
        self.assertEqual(animal.especie, "Cachorro")
        self.assertEqual(animal.idade, 3)

    def test_consultar_animal(self):
        Animal.objects.create(
            nome="Rex",
            especie="Cachorro",
            idade=5
        )

        animal = Animal.objects.get(nome="Rex")

        self.assertEqual(animal.nome, "Rex")

    def test_pagina_inicial(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_lista_animais(self):
        response = self.client.get("/animais/")
        self.assertEqual(response.status_code, 200)

    def test_cadastro_animal(self):
        response = self.client.post(
            "/animais/novo/",
            {
                "nome": "Luna",
                "especie": "Gato",
                "idade": "2"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Animal.objects.filter(nome="Luna").exists()
        )
