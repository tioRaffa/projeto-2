import os
from django.views.generic import ListView, DetailView

from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import RecipesModels, Category
from django.http import Http404
from django.db.models import Q
from utils.test_pagination.pagination import make_pagination
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

PER_PAGE = int(os.environ.get('PER_PAGE'))


class RecipeListViewBase(ListView):
    model = RecipesModels
    template_name = 'receitas/pages/home.html'
    context_object_name = 'dados'
    paginate_by = None
    ordering = '-id'
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        queryset = queryset.select_related('author', 'category')

        return queryset
        
    
    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = make_pagination(self.request, ctx.get('dados'), PER_PAGE, 4)
        
        ctx.update({
            'dados': page_obj,
            'pagination_range': pagination_range,
            'is_detail_page': False
        })
                
        
        return ctx
    
    
class Category(RecipeListViewBase):
    template_name = 'receitas/pages/category.html'
    

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(
            category__id=self.kwargs.get('id')
        )
        
        return queryset


    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = make_pagination(self.request, ctx.get('dados'), PER_PAGE, 4)
        title = self.get_queryset(*args, **kwargs)
        
        ctx.update({
            'dados': page_obj,
            'pagination_range': pagination_range,
            'is_category_page': True,
            'is_detail_page': False,
            'title': f'{title[0].category.name}'
            })        
        
        return ctx
    

class Search(RecipeListViewBase):
    template_name = 'receitas/pages/search.html'
    
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        
        search_term = self.request.GET.get('q', '').strip()
        queryset = queryset.filter(
            Q(
                Q(title__icontains=search_term) | 
                Q(category__name__icontains=search_term),
            ),
            is_published=True
            )
        
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = make_pagination(self.request, ctx.get('dados'), PER_PAGE, 4)
        search_term = self.request.GET.get('q', '').strip()
        
        ctx.update({
            'page_title': f'Search for "{search_term}"',
            'search_term': search_term,
            'dados': page_obj,
            'pagination_range': pagination_range,
            'add_url_query': f'&q={search_term}',
        })
        
        return ctx
    

class RecipeDetail(DetailView):
    model = RecipesModels
    template_name = 'receitas/pages/receita_view.html'
    context_object_name = 'dado'

    
    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        
        ctx.update({
            'is_datail_page': True
        })
        
        return ctx
    
    
def theory(request):
    recipe = RecipesModels.objects.all()
    context = {
        'recipes': recipe
    }
    return render(request, 'receitas/pages/theory.html', context=context)


def custom_404(request, exception):
    return render(request, 'receitas/pages/error_404.html', status=404)
def skull(request):
    return render(request, 'receitas/pages/skull.html')