from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dt_nascimento = models.DateField()

    def __str__(self):
        return self.nome