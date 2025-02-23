from django.test import TestCase
from core.models import Category, RecipesModels, User

class RecipeTestBase(TestCase):
    def setUp(self):
        
        
        return super().setUp()
    
    
    def create_category(self, name='category'):
        return Category.objects.create(name=name)
    
    
    def create_user(
        self, first_name='user',
            last_name='user',
            username='user nme',
            password='user123',
            email='user@gmail.com',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
        
        
    def create_recipe(
        self, category=None,
            author=None,
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
    ):
        if category is None:
            category_data = {}
            
        if author is None:
            author_data = {}
            
        return RecipesModels.objects.create(
            category=self.create_category(**category_data),
            author=self.create_user(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published
        )