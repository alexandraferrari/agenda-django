# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

# Create your views here.
def hello(req, nome):
  return HttpResponse('<h1>Hello {}<h1>'.format(nome))

def soma(req, a, b):
  soma = int(a) + int(b)
  return HttpResponse('<h1>{} + {} = {}<h1>'.format(a, b, soma))

def subtrai(req, a, b):
  subtrai = a - b
  return HttpResponse('<h1>{} - {} = {}'.format(a, b, subtrai))

def multiplica(req, a, b):
  multiplica = a * b
  return HttpResponse('<h1>{} * {} = {}'.format(a, b, multiplica))

def divide(req, a, b):
  divide = a / b
  return HttpResponse('<h1>{} / {} = {}'.format(a, b, divide))

def index(req):
  return redirect('/agenda')

def getEventos(req, titulo):
  evento = Evento.objects.get(titulo = titulo)
  return HttpResponse('<h1>{}'.format(evento.descricao))

def lista_eventos(req):
  usuario = req.user
  evento = Evento.objects.filter(usuario=usuario)
  dados = { 'eventos': evento }
  return render(req, 'agenda.html', dados)
