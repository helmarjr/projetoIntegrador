from django.db import models

# Create your models here.


class Responsavel(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome




