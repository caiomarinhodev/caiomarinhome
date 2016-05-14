from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    mensagem = models.TextField(blank=False)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.nome).upper() + str(self.sobrenome).upper()