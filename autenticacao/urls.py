from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),   
    path('servicos/', views.servicos, name='servicos'),
    path('produtos/', views.produtos, name='produtos')
]