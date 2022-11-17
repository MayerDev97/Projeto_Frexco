from django.db import models
from random import choice
import string

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=100)
    ativa = models.BooleanField(default=True)
    senha = models.CharField(max_length=15, null=True, blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    if senha == '':
        for i in range(5):
            senha += choice(string.ascii_lowercase)

    def __str__(self) -> str:
        return self.nome_completo