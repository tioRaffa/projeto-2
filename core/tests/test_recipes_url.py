from django.test import TestCase
from django.urls import reverse


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