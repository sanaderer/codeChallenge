from django.shortcuts import render

# Create your views here.
def cadastro(request):
    match request.method:
        case 'GET':
            pass