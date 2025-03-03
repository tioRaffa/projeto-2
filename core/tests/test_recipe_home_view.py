from django.test import TestCase
from django.urls import reverse, resolve
from core import views
from utils.recipes.factory import make_recipe

from .recipe_test_base import RecipeTestBase

    
class RecipeHomeViewsTest(RecipeTestBase):
    
    def test_recipe_home_view(self):
        view = resolve('/')
        
        self.assertIs(view.func, views.MyView)
        
    def test_recipe_home_status_code_200(self):
        response = self.client.get(reverse('recipes_home'))
        self.assertEqual(response.status_code, 200)
   
        

        