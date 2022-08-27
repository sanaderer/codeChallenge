from django.urls import path
from . import views

urlpatterns = [
    path('auth/cadastro/', views.cadastro, name='cadastro'),
    path('index', views.index, name='index'),   
    path('servicos', views.servicos, name='servicos'),
    path('produtos', views.produtos, name='produtos'),
    path('formulario', views.formulario, name='formulario'),
    path('addprodutos', views.addprodutos, name='addprodutos')
]