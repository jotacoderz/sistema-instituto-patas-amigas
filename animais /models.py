from django.db import models


class Animal(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    idade = models.PositiveIntegerField(null=True, blank=True)
    data_cadastro = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.nome
