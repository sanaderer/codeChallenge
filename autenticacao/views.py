from django.shortcuts import render
from django.http import HttpResponse
from autenticacao.models import Cliente
from autenticacao.forms import ClienteForm


# Create your views here.
def index(request):
    return render(request, 'index.html')
    match request.method:
        case 'GET':
            pass

def servicos(request):
    return render(request, 'servicos.html')
    match request.method:
        case 'GET':
            pass

def produtos(request):
    return render(request, 'produtos.html')
    match request.method:
        case 'GET':
            pass

def formulario(request):
    data = {}
    data['formulario'] = ClienteForm()
    return render(request, 'formulario.html', data)
    match request.method:
        case 'GET':
            pass
