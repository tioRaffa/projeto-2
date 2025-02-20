from django.test import TestCase
from django.urls import reverse, resolve
from core import views


class RecipeViewsTest(TestCase):
    def test_recipe_home_view(self):
        view = resolve('/')
        
        self.assertIs(view.func, views.MyView)
        
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