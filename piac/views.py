from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import OportunidadeRecentes, OrdensDeServico
from django.contrib.auth import logout
from .forms import createOportunidadeForm, createOrdemForm

def piachome(request):
    return render(request, 'piac_home.html')


@login_required
def listarOportunidades(request):
    termo_busca = request.GET.get('pesquisa', None)

    if termo_busca:
        dados = OportunidadeRecentes.objects.all()
        dados = dados.filter(nome__icontains = termo_busca)
    else:
        dados = OportunidadeRecentes.objects.all()

    return render(request, 'listar_oport.html', {'dados':dados})


@login_required
def listarOrdens(request):
    termo_busca = request.GET.get('pesquisa')
    if termo_busca:
        dados = OrdensDeServico.objects.all()
        dados = dados.filter(numero__cod_projeto__icontains = termo_busca)
    else:
        dados = OrdensDeServico.objects.all()

    return render(request, 'listar_ord.html', {'dados':dados})

@login_required
def deletarOportunidade(request, id):
    query = get_object_or_404(OportunidadeRecentes,pk=id)
    form = createOportunidadeForm(request.POST or None, instance=query)

    if request.method == 'POST':
        query.delete()
        return redirect('lista_oportunidades')

    return render(request,'deletar_oport.html', {'form':form})

@login_required
def deletarOrdem(request, numero):
    query = OrdensDeServico.objects.filter(numero__cod_projeto = numero)
    #query = get_object_or_404(OrdensDeServico,pk=numero)

    if request.method=='POST':
        query.delete()
        return redirect('lista_ordens')

    return render(request,'deletar_ord.html', {'dado':query})


def mylogout(request):
    logout(request)
    return redirect('piac_home')


@login_required
def myOportunidade(request):
    form = createOportunidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_oportunidades')

    return render(request, 'criar_oport.html', {'form':form})


@login_required
def detailOportunidade(request, id):
    query = get_object_or_404(OportunidadeRecentes, pk=id)
    form = createOportunidadeForm(request.POST or None, instance=query)

    if form.is_valid():
        form.save()
        return redirect('lista_oportunidades')

    return render(request, 'criar_oport.html', {'form':form})

@login_required
def detailOrdem(request, numero):
    query = OrdensDeServico.objects.get(numero__cod_projeto = numero)
    form = createOrdemForm(request.POST or None, instance=query)

    if form.is_valid():
        form.save()
        return redirect('lista_ordens')

    return render(request, 'criar_ord.html', {'form':form})

@login_required
def myOrder(request, id):
    query = get_object_or_404(OportunidadeRecentes, pk=id)
    #tentar arrumar um jeito de passar para o formulario o valor do numero da oportunidade
    form = createOrdemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_ordens')

    return render(request, 'criar_ord.html', {'form':form})
