# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

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