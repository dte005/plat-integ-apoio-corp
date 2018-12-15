from django.urls import path
from .views import piachome, listarOportunidades, mylogout, myOportunidade, detailOportunidade, myOrder, listarOrdens, deletarOportunidade, deletarOrdem

urlpatterns = [
    path('home/', piachome, name='piac_home'),
    path('listaop/', listarOportunidades, name='lista_oportunidades'),
    path('logout/', mylogout, name='logout'),
    path('criarordem/<int:id>', myOrder, name='criar_ordem'),
    path('criarop/', myOportunidade, name='criar_op'),
    path('listarordens/', listarOrdens, name='lista_ordens'),
    path('deletarord/<str:numero>', deletarOrdem, name='deletar_ordem'),
    path('deletarop/<int:id>', deletarOportunidade, name='deletar_op'),
    path('detalharop/<int:id>', detailOportunidade, name='detalhar_op'),
]
