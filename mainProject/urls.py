from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from biblioteca.api import LivroViewSet, EmprestimoViewSet
from users.api import UsuarioViewSet
from biblioteca.api_views import DevolucaoViewSet

# responsável por definir as urls padrões do projeto e da API
router = routers.DefaultRouter()
router.register(r'livros', LivroViewSet)
router.register(r'emprestimos', EmprestimoViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'devolucao', DevolucaoViewSet, basename='devolucao')

urlpatterns = [
    path('', views.home, name='home'), 
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('users.urls')), 
    path('biblioteca/', include('biblioteca.urls'))
]
