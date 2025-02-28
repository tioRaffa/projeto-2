from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import RecipesModels, Category
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from utils.test_pagination.pagination import make_pagination_range
# Create your views here.


def MyView(request):
    recipes = get_list_or_404(RecipesModels.objects.filter(
        is_published=True).order_by('-id'))

    
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(recipes, 9)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        paginator.page_range,
        4,
        current_page
    )
    
    
    context = {
        'dados': page_obj,
        'is_detail_page': False,
        'pagination_range': pagination_range
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


def search(request):
    
    search_term = request.GET.get('q', '').strip()
    
    if not search_term:
        raise Http404
    
    try:
        category = Category.objects.filter(name=search_term)
    except Category.DoesNotExist:
        category = None
    
    
    recipes = RecipesModels.objects.filter(
        Q(
            Q(title__icontains=search_term) | 
            Q(category__name__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')
    
    
    context = {
        'page_title': f'Search for "{search_term}"',
        'search_term': search_term,
        'dados': recipes,
    }
    
    return render(request, 'receitas/pages/search.html', context=context)



def custom_404(request, exception):
    return render(request, 'receitas/pages/error_404.html', status=404)

