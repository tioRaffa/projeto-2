from django.test import TestCase
from django.urls import reverse, resolve
from core import views

from .recipe_test_base import RecipeTestBase

    
class RecipeViewsTest(RecipeTestBase):
    
    def test_recipe_home_view(self):
        view = resolve('/')
        
        self.assertIs(view.func, views.MyView)
        
    def test_recipe_home_status_code_200(self):
        response = self.client.get(reverse('recipes_home'))
        self.assertEqual(response.status_code, 200)
        
        
    def test_recipe_login_view(self):
        view = resolve('/login/')
        
        self.assertIs(view.func, views.login)
        
        
    def test_recipe_detail_page_view(self):
        detail_pg_view = resolve(
            reverse('recipe_detail_page', kwargs={'id': 1})
        )
        
        self.assertIs(detail_pg_view.func, views.recipes)
    
    
    def test_recipe_category_view(self):
        category_view = resolve(
            reverse('category', kwargs={'id': 1})
        )
        
        self.assertIs(category_view.func, views.category)
    
        
    def test_recipe_login_text(self):
        response = self.client.get(reverse('login'))
        
        self.assertIn(
            '<span class="details">Confirm Password</span>',
            response.content.decode('utf-8')
        )
        
    # 404
    def test_recipe_category_view_404(self):
        response = self.client.get(reverse('category', kwargs={'id': 10}))
        
        self.assertEqual(response.status_code, 404)
    
    def test_recipe_detail_page_404(self):
        response = self.client.get(reverse('recipe_detail_page', kwargs={'id': 10}))
        
        self.assertEqual(response.status_code, 404)
     
        
    # load template
    def test_recipe_home_template_loads_recipes(self):
        self.create_recipe()
        
        response = self.client.get(reverse('recipes_home'))
        content = response.content.decode('utf-8')
        
        response_recipe = response.context['dados']
        
        
        self.assertEqual(response_recipe[0].title, 'Recipe Title')
        ...
        
    
    def  test_category_template_loads(self):
        tittle = 'Category Test'
        
        self.create_recipe(title=tittle)
        
        response = self.client.get(reverse('category', args=(4,)))
        response_cateory = response.context['dados']
        
        self.assertIn(response_cateory[0].title, tittle)
    
    
