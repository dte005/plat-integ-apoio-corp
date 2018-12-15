from django.shortcuts import render
from .models import Funcionario

def pbhome(request):
    return render(request, 'pb_home.html')

def pblista(request):
    dados = Funcionario.objects.all()
    return render(request, 'lista_func.html', {'dados':dados})
