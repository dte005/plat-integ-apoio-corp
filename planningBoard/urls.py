from django.urls import path
from .views import pbhome, pblista

urlpatterns = [
    path('home/', pbhome, name='pb_home'),
    path('listafunc/', pblista, name='listar_funcionario'),
]
