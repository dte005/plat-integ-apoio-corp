from django.forms import ModelForm
from .models import Funcionario

class createFuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'funcao', 'departamento', 'foto']
