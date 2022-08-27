from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        pass

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