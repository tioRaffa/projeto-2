from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Create your views here.


def MyView(request):
    context = {
        'dados': [make_recipe() for _ in range(10)],
        'is_detail_page': False,
    }
    return render(request, 'receitas/pages/home.html', context)


def recipes(request, id):
    context = {
        'dado': make_recipe(),
        'is_datail_page': True,
    }
    return render(request, 'receitas/pages/receita_view.html', context)


def login(request):
    return render(request, 'receitas/pages/login.html')
