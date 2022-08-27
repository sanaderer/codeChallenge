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

