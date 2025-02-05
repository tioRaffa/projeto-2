from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse
# Create your views here.


def MyView(request):
    context = {
        'nome': 'Rafael'
    }
    return render(request, 'home.html', context)


def login(request):
    return render(request, 'login.html')
