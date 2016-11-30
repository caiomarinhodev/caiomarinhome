from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext

from app.models import *


def index(request):
    projetos = Projeto.objects.filter(visivel=True).order_by('-criado_em')[:3]
    return render_to_response('index.html', {'projetos': projetos},
                              context_instance=RequestContext(request))


def projetos(request):
    projetos = Projeto.objects.filter(visivel=True)
    return render_to_response('projetos.html', {'projetos': projetos},
                              context_instance=RequestContext(request))


def ver_projeto(request, id):
    return render_to_response('ver_projeto.html', {'projeto': get_object_or_404(Projeto, id=id)},
                              context_instance=RequestContext(request))


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
        return render(request, 'base.html', {'error': 'Algum dado informado esta invalido.'})
    return render(request, 'base.html', {'success': 'Mensagem enviada!'})
