from django.contrib import admin
from .models import Category, RecipesModels
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(RecipesModels)
class RecepiesModelsAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
