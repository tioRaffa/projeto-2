from django.test import TestCase
from django.urls import reverse, resolve
from core import views

from .recipe_test_base import RecipeTestBase

    
class RecipeViewsTest(RecipeTestBase):
    

        
        
    def test_recipe_detail_page_view(self):
        detail_pg_view = resolve(
            reverse('recipe_detail_page', kwargs={'id': 1})
        )
        
        self.assertIs(detail_pg_view.func, views.recipes)
    

        
    # 404
    def test_recipe_detail_page_404(self):
        response = self.client.get(reverse('recipe_detail_page', kwargs={'id': 201}))
        
        self.assertEqual(response.status_code, 404)
     
    def test_recipe_search_404_view(self):
        response = self.client.get(reverse('search_box'))
        
        self.assertEqual(response.status_code, 404)
    
