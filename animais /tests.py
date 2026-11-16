from django.test import TestCase
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
