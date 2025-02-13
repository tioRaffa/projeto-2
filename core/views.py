from django.shortcuts import render
from utils.recipes.factory import make_recipe

from .models import RecipesModels
# Create your views here.


def MyView(request):
    recipes = RecipesModels.objects.filter(is_published=True).order_by('-id')
    context = {
        'dados': recipes,
        'is_detail_page': False,
    }
    return render(request, 'receitas/pages/home.html', context)


def recipes(request, id):
    recipes = RecipesModels.objects.all().get(id=id)
    context = {
        'dado': recipes,
        'is_datail_page': True,
    }
    return render(request, 'receitas/pages/receita_view.html', context)


def category(request, id):
    receitas = RecipesModels.objects.filter(
        id=id, is_published=True).order_by('-id')
    context = {
        'dados': receitas,
        'is_category_page': True,
        'is_detail_page': False,
    }
    return render(request, 'receitas/pages/category.html', context)


def login(request):
    return render(request, 'receitas/pages/login.html')
