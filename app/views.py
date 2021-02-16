from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from app.models import *


class IndexView(ListView):
    template_name = 'index.html'
    model = Projeto
    context_object_name = 'projetos'

    def get_queryset(self):
        return Projeto.objects.filter(visivel=True).order_by('-criado_em')[:3]


class ListProjetos(ListView):
    template_name = 'projetos.html'
    model = Projeto
    context_object_name = 'projetos'

    def get_queryset(self):
        return Projeto.objects.filter(visivel=True)


class ViewProjeto(DetailView):
    model = Projeto
    template_name = 'ver_projeto.html'
    context_object_name = 'projeto'


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
        return redirect('index')
    return redirect('index')
