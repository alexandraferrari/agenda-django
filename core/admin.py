# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
  '''
    Define os campos que serão exibidos na tela de admin
  '''
  list_display = ('titulo', 'data_evento', 'data_criacao')
  list_filter = ('titulo', 'data_evento')

admin.site.register(Evento, EventoAdmin)