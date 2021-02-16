from __future__ import unicode_literals

from base64 import b64encode

import pyimgur
from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.


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
    texto = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)
    visivel = models.BooleanField(default=True)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.titulo)

    def __unicode__(self):
        return u'%s' % (self.titulo)


class Foto(models.Model):
    file = models.FileField(blank=True, null=True)
    foto = models.URLField(blank=True, null=True, default='https://placehold.it/300x300')
    model = models.ForeignKey(Projeto, blank=True, null=True, on_delete=models.CASCADE)
    principal = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            CLIENT_ID = "cdadf801dc167ab"
            bencode = b64encode(self.file.read())
            client = pyimgur.Imgur(CLIENT_ID)
            r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': bencode})
            file = r['link']
            self.foto = file
        except (Exception,):
            pass
        super(Foto, self).save(force_insert=force_insert, force_update=force_update, using=using,
                               update_fields=update_fields)
