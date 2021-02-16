from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from app.models import *


class ProjetoForm(forms.ModelForm):
    texto = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Projeto
        exclude = ['']


class FotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'foto',)


class FotoInline(admin.TabularInline):
    model = Foto


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
    list_filter = ('nome',)


class ProjetoAdmin(admin.ModelAdmin):
    inlines = [FotoInline, ]
    list_display = ('titulo', 'id', 'criado_em', 'visivel')
    ordering = ['-criado_em']


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)
admin.site.register(Foto, FotoAdmin)
admin.site.register(Projeto, ProjetoAdmin)
