from django.shortcuts import render, get_object_or_404, redirect
from .models import Funcionario
from .forms import createFuncionarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def pblista(request):
    termo_busca = request.GET.get('pesquisa' or None)

    if termo_busca:
        dados = Funcionario.objects.all()
        dados = dados.filter(nome__icontains = termo_busca)
    else:
        dados = Funcionario.objects.all()

    return render(request, 'lista_func.html', {'dados':dados})



def listasuper(request):
    dados = User.objects.all()
    return render(request, 'lista_super.html', {'dados':dados})


@login_required
def detailfunc(request, id):
    query = get_object_or_404(Funcionario, pk=id)
    form = createFuncionarioForm(request.POST or None, request.FILES or None, instance=query)

    if form.is_valid():
        form.save()
        return redirect('listar_funcionario')

    return render(request, 'criar_func.html', {'form':form})


@login_required
def criarfunc(request):
    form = createFuncionarioForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listar_funcionario')

    return render(request, 'criar_func.html', {'form':form})
