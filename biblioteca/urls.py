from django.urls import path
from . import views

# urls principais dentro do app biblioteca
app_name = 'biblioteca'

urlpatterns = [
    path('', views.biblioteca, name='home'), 
    path('livros/', views.listar_livros, name='listar_livros'), 
    path('emprestimo/', views.criar_emprestimo, name='criar_emprestimo'), 
    path('emprestimos/<int:id>/devolver/', views.devolver_livro, name='devolver_livro'),
]