from django.shortcuts import render
from utils.recipes.factory import make_recipe

from .models import RecipesModels
# Create your views here.


def MyView(request):
    recipes = RecipesModels.objects.all().order_by('-id')
    context = {
        'dados': recipes,
        'is_detail_page': False,
    }
    return render(request, 'receitas/pages/home.html', context)


def recipes(request, id):
    context = {
        'dado': make_recipe(),
        'is_datail_page': True,
    }
    return render(request, 'receitas/pages/receita_view.html', context)


def category(request, id):
    receita = RecipesModels.objects.get(id=id)
    context = {
        'dado': receita
    }
    return render(request, 'receitas/pages/receita_view.html', context)


def login(request):
    return render(request, 'receitas/pages/login.html')
