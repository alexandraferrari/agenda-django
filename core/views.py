# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# def index(req):
#   return redirect('/agenda')

def getEventos(req, titulo):
  evento = Evento.objects.get(titulo = titulo)
  return HttpResponse('<h1>{}'.format(evento.descricao))

def login_user(req):
  return render(req, 'login.html')

def logout_user(req):
  logout(req)
  return redirect('/')


def submit_login(req):
  if req.POST:
    username = req.POST.get('username')
    password = req.POST.get('password')
    usuario = authenticate(username=username, password=password)
    if usuario is not None:
      login(req, usuario)      
      return redirect('/')
    else:
      messages.error(req, "Usuário ou senha inválidos")
  
  return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(req):
  usuario = req.user
  evento = Evento.objects.filter(usuario=usuario)
  dados = { 'eventos': evento }
  return render(req, 'agenda.html', dados)
