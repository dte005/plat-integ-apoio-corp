from django.db import models
from planningBoard import models as base

class OportunidadeRecentes(models.Model):
    nome = models.CharField(max_length=30)
    cod_projeto = models.CharField(max_length=30)
    descricao = models.TextField()
    CHOICES = (
    ('SR', 'Serviço'),
    ('PJ', 'Projeto'),)
    tipo = models.CharField(max_length=2,
        choices=CHOICES,
        default='Serviço',)

    def __str__(self):
        return str(self.cod_projeto)


class OrdensDeServico(models.Model):
    numero = models.OneToOneField(OportunidadeRecentes,on_delete=models.CASCADE, primary_key=True)
    recursos = models.ManyToManyField(base.Funcionario)
    jsa_status = models.BooleanField(default=False)
    crol_status = models.BooleanField(default=False)
    rels_status = models.BooleanField(default=False)
    reld_status = models.BooleanField(default=False)
    gpg_status = models.BooleanField(default=False)
    mobile_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.numero)
