from django.shortcuts import render, redirect
from app.models import *


def index(request):
    return render(request, 'index.html')

def submit(request):
    data = request.POST
    nome = data.get('nome')
    sobrenome = data.get('sobrenome')
    mensagem = data.get('mensagem')
    email = data.get('email')
    objeto = Contato(nome=nome, sobrenome=sobrenome, email=email, mensagem=mensagem)
    try:
        objeto.save()
    except:
        return render(request, 'index.html', {'error': 'Algum dado informado esta invalido.'})
    return render(request, 'index.html', {'success': 'Mensagem enviada!'})
