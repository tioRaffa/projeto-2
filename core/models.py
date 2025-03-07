from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Author(models.Model):
    pass


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class RecipesModels(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150, null=True)
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/cover/%y/%m/%d', blank=True, null=True)

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
