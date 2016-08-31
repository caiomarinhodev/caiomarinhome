from __future__ import unicode_literals
from cloudinary.models import CloudinaryField

from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
from django.db.models import permalink


class Contato(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    mensagem = models.TextField(blank=False)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.nome).upper() + str(self.sobrenome).upper()


class Categoria(models.Model):
    tag = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.tag)


class Projeto(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    desc = models.TextField(max_length=200)
    texto = RichTextField()
    categoria = models.ForeignKey(Categoria, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)
    visivel = models.BooleanField(default=True)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.titulo)

    def __unicode__(self):
        return u'%s' % (self.titulo)


class Foto(models.Model):
    foto = CloudinaryField('imagem')
    model = models.ForeignKey(Projeto)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)
