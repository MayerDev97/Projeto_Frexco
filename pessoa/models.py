from django.db import models

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=100)
    ativa = models.BooleanField(default=True)
    senha = models.CharField(max_length=15, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
