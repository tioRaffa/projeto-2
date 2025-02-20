from django.test import TestCase
from core.models import Category, RecipesModels, User

class RecipeTestBase(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Teste')
        
        user = User.objects.create_user(
            first_name='user',
            last_name='user',
            username='user nme',
            password='user123',
            email='user@gmail.com',
            
        )
        
        recipe = RecipesModels.objects.create(
            category=category,
            author=user,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='munitos',
            servings=5,
            servings_unit='Porcoes',
            preparation_steps='recipe preparation steps',
            preparation_steps_is_html=False,
            is_published=True
        )        
        
        return super().setUp()