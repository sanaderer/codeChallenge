from django.urls import path
from . import views

urlpatterns = [
    path('auth/cadastro/', views.cadastro, name='cadastro'),
]