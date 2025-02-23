from django.test import TestCase
from django.urls import reverse, resolve
from core import views


class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes_home')
        
        self.assertEqual(url, '/')
    
    
    def test_recipe_category_url_is_correct(self):
        category_url = reverse('category', kwargs={'id': 1})
        
        self.assertEqual(category_url, '/recipes/category/1/')
    
    def test_recipe_detail_url_is_correct(self):
        detail_url = reverse('recipe_detail_page', kwargs={'id': 2})
        
        self.assertEqual(detail_url, '/recipes/2/')
        
    def test_recipe_search_box_url_connect(self):
        search_url = reverse('search_box')
        
        self.assertEqual(search_url, '/recipes/search/')
        
    def test_recipe_search_box_views(self):
        search_view = resolve(
            reverse('search_box')
        )
        self.assertIs(search_view.func, views.search)
        
    
    def test_recipe_search_box_load_template(self):
        
        response = self.client.get(reverse('search_box') + '?q=teste')
        
        self.assertTemplateUsed(response, 'receitas/pages/search.html')
        ...