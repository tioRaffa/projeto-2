from django.contrib import admin
from .models import Category, RecipesModels
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(RecipesModels)
class RecepiesModelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'author', 'created_at', 'is_published')
    list_display_links = 'id', 'title', 'created_at',
    search_fields = 'id', 'title', 'author', 'is_published',
    list_filter = 'id', 'title', 'author', 'category', 'is_published',
    list_per_page = 10
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('title',)
    }

admin.site.register(Category, CategoryAdmin)
