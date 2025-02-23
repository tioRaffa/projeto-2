from django.test import TestCase
from django.urls import reverse, resolve
from core import views

from .recipe_test_base import RecipeTestBase

    
class RecipeCategoryViewsTest(RecipeTestBase):
    
    def test_recipe_category_view(self):
        category_view = resolve(
            reverse('category', kwargs={'id': 1})
        )
        
        self.assertIs(category_view.func, views.category)
    
    def test_recipe_category_view_404(self):
        response = self.client.get(reverse('category', kwargs={'id': 10}))
        
        self.assertEqual(response.status_code, 404)
        
    def test_category_template_loads(self):
        tittle = 'Category Test'
        
        self.create_recipe(title=tittle)
        
        response = self.client.get(reverse('category', args=(4,)))
        response_cateory = response.context['dados']
        
        self.assertIn(response_cateory[0].title, tittle)
