from django.urls import path
from . import views

app_name = 'emprestimos'

urlpatterns = [
    path('inserir_emprestimo/', views.inserir_emprestimo, name='inserir_emprestimo'),
    path('listar_emprestimos/', views.listar_emprestimos, name='listar_emprestimos'),

]