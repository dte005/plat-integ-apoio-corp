from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=30)
    funcao = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)
    foto = models.ImageField(upload_to='foto_cliente', null=True, blank=True)

    def __str__(self):
        return self.nome
