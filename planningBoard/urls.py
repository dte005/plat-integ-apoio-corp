from django.urls import path
from .views import pblista, detailfunc, criarfunc, listasuper

urlpatterns = [
    path('listafunc/', pblista, name='listar_funcionario'),
    path('detalharfunc/<int:id>', detailfunc, name='detalhar_func'),
    path('criarfunc/', criarfunc, name='criar_func'),
    path('listasuper/', listasuper, name='lista_super'),
]
