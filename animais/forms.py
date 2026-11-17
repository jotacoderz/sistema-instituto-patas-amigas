from django import forms
from .models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ["nome", "especie", "idade"]

        labels = {
            "nome": "Nome do animal",
            "especie": "Espécie",
            "idade": "Idade",
        }

        widgets = {
            "nome": forms.TextInput(attrs={
                "placeholder": "Ex.: Mel"
            }),
            "especie": forms.TextInput(attrs={
                "placeholder": "Ex.: Cachorro"
            }),
            "idade": forms.NumberInput(attrs={
                "min": 0,
                "placeholder": "Idade em anos"
            }),
        }
