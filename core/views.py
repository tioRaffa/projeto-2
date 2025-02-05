from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse
# Create your views here.


def MyView(request):
    context = {
        'nome': 'Rafael'
    }
    return render(request, 'home.html', context)


def contato(request):
    return render(request, 'contato.html')


def sobre(request):
    return render(request, 'sobre.html')
