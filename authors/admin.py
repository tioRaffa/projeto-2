from django.contrib import admin

# Register your models here.

from .models import ProfileModels

@admin.register(ProfileModels)
class ProfileModelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'bio']
    ordering = ['-id']
    list_display_links = ['id', 'person']
    
    