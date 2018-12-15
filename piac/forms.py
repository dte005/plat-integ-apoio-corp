from django.forms import ModelForm
from .models import OportunidadeRecentes, OrdensDeServico

class createOportunidadeForm(ModelForm):
    class Meta:
        model = OportunidadeRecentes
        fields = ['nome', 'cod_projeto', 'descricao', 'tipo']

class createOrdemForm(ModelForm):
    class Meta:
        model = OrdensDeServico
        fields = ['numero', 'recursos', 'jsa_status', 'crol_status', 'rels_status', 'reld_status', 'gpg_status', 'mobile_status']
