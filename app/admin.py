from django.contrib import admin
from app.models import *

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
    list_filter = ('nome',)


admin.site.register(Contato, ContatoAdmin)