from django.views.generic import TemplateView
from core.models import RecipesModels, Category

from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, reverse, get_object_or_404
from authors.models import ProfileModels
from django.contrib import messages




class Profile(TemplateView):
    template_name = "authors/pages/profile.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        profile_id = context.get('id')
        profile = get_object_or_404(ProfileModels.objects.filter(id=profile_id).select_related('person'), id=profile_id)
        
        context = {
            **context,
            'profile': profile
        }
        
        return self.render_to_response(context=context)