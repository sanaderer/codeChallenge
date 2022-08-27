from django.shortcuts import render, redirect
from django.http import HttpResponse
from autenticacao.models import Cliente
from autenticacao.forms import ClienteForm
from .utils import Valida
import datetime

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
    match request.method:
        case 'GET':
            data = {}
            data['formulario'] = ClienteForm()
            return render(request, 'formulario.html', data)

        case 'POST':
            form = ClienteForm(request.POST)
            nome = form.data.get('nome')
            cpf = form.data.get('cpf')
            data_nascimento = form.data.get('data_nascimento')
            telefone = form.data.get('telefone')
            email = form.data.get('email')

            print('telefone', telefone)

            branco = Valida.branco(nome, cpf, data_nascimento, telefone, email)
            if branco:
                return redirect('/formulario')

            if not Valida.cpf(cpf):
                return redirect('/formulario')

            numero_valido, numero_formatado = Valida.numero(telefone.replace(' ', ''))
            print('numero formatado', numero_formatado)
            if not numero_valido:
                return redirect('/formulario')

            if not Valida.email(email):
                return redirect('/formulario')

            try:
                cliente = Cliente(
                    nome=nome,
                    cpf=cpf.replace('.', '').replace('-', ''),
                    data_nascimento=data_nascimento,
                    telefone=numero_formatado,
                    email=email
                )
                cliente.save()

                return redirect('/formulario')

            except:
                return redirect('/formulario')
    

def addprodutos(request):
    return render(request, 'addprodutos.html')
    match request.method:
        case 'GET':
            pass