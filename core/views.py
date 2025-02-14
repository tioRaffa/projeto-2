from django.shortcuts import render, get_object_or_404, get_list_or_404
from utils.recipes.factory import make_recipe
from .models import RecipesModels
# Create your views here.


def MyView(request):
    recipes = get_list_or_404(RecipesModels.objects.filter(
        is_published=True).order_by('-id'))

    context = {
        'dados': recipes,
        'is_detail_page': False,
    }

    return render(request, 'receitas/pages/home.html', context)


def recipes(request, id):
    # recipes = RecipesModels.objects.all().get(id=id)
    recipes = get_object_or_404(RecipesModels, id=id, is_published=True)

    context = {
        'dado': recipes,
        'is_datail_page': True,
        'title': f'{recipes.title}'
    }

    return render(request, 'receitas/pages/receita_view.html', context)


def category(request, id):
    receitas = get_list_or_404(RecipesModels.objects.filter(
        category__id=id, is_published=True).order_by('-id'))

    context = {
        'dados': receitas,
        'is_category_page': True,
        'is_detail_page': False,
        'title': f'{receitas[0].category.name}'
    }

    return render(request, 'receitas/pages/category.html', context)


def login(request):
    return render(request, 'receitas/pages/login.html')


def custom_404(request, exception):
    return render(request, 'receitas/pages/error_404.html', status=404)
