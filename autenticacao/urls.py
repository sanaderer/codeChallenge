from django.urls import path
from . import views

urlpatterns = [

    path('index', views.index, name='index'),   
    path('servicos', views.servicos, name='servicos'),
    path('produtos', views.produtos, name='produtos'),
    path('formulario', views.formulario, name='formulario'),
    path('addprodutos', views.addprodutos, name='addprodutos'),
    path('index/', views.index, name='index'),   
    path('servicos/', views.servicos, name='servicos'),
    path('produtos/', views.produtos, name='produtos'),
    path('formulario/', views.formulario, name='formulario'),
    path('addcçoemte/', views.addcliente, name='addcliente'),

]