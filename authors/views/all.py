from core.models import RecipesModels, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from authors.forms import RegisterForm, LoginForms, AuthorRecipeForm, AuthorCreateRecipe
from django.contrib import messages
from django.utils.text import slugify
import time


def register_view(request):
    
    if str(request.method) == 'POST':
        form = RegisterForm(request.POST or None)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            
            form = RegisterForm()
            messages.success(request, 'Registro Concluido Com Sucesso')
            return redirect('authors:RegisterView')
        
        else:
            messages.error(request, 'Registro Não Concluido')
            
    else:
        form = RegisterForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'authors/pages/register_view.html', context=context)


def login_(request):
    form = LoginForms()
    
    if str(request.method) == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            is_authenticated = authenticate(
                username=username,
                password=password,
            )
            
            if is_authenticated is not None:
                login(request, is_authenticated)
                return redirect(reverse('authors:dashboard'))
            
            else:
                messages.error(request, 'Erro! Digite a senha novamente')            
    

    context = {
        'form': form
    }
    
    return render(request, 'authors/pages/login.html', context=context)


@login_required(login_url='authors:login', redirect_field_name='next')
def logout_user(request):
    
    if str(request.method) != 'POST':
        return redirect(reverse('authors:login'))
    
    if request.POST.get('username') != request.user.username:
        return redirect(reverse('authors:login'))
        
    
    logout(request)
    return redirect(reverse('recipes_home'))


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_user(request):
    
    recipe_false = RecipesModels.objects.filter(
        is_published=False,
        author=request.user,
    )
    recipe_true = RecipesModels.objects.filter(
        is_published=True,
        author=request.user,
    )
    
    
    context = {
        'recipes_false': recipe_false,
        'recipes_true': recipe_true,
        'author': request.user,
    }
    
    return render(request, 'authors/pages/dash_board.html', context=context)


def dashboard_edition(request, id):
    author = request.user
    recipe = get_object_or_404(RecipesModels, id=id, author=author)
    
    
    
    form = AuthorRecipeForm(instance=recipe)
    
    
    if str(request.method) == 'POST':
        # form = AuthorRecipeForm(data=request.POST, request.FILES, instance=recipe)
        form = AuthorRecipeForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=recipe
        )
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = author
            recipe.preparation_steps_is_html = False
            recipe.is_published = False
            recipe.category = Category.objects.get(id=recipe.category.id)

            recipe.save()
            messages.success(request, 'Alteração concluida com SUCESSO!')
            return redirect(reverse('authors:dashboard'))
            
        else:
            messages.error(request, f'ERRO, Tente novamente! ')
            print(form.errors)
            form = AuthorRecipeForm()
        
        
    context = {
        'recipes': recipe,
        'forms': form,
        'categorys': Category.objects.all()
    }
    
    return render(request, 'authors/pages/dash_board_editor.html', context=context)


def dashboard_create_recipe(request):
    form = AuthorCreateRecipe()
    
    if str(request.method) == 'POST':
        form = AuthorCreateRecipe(data=request.POST, files=request.FILES)
        
        if form.is_valid():
            recipe: RecipesModels = form.save(commit=False)
            recipe.author = request.user
            recipe.preparation_steps_is_html = False
            recipe.is_published = False
            recipe.slug = slugify(recipe.title)
            
            recipe.save()
            form = AuthorCreateRecipe()
            
            messages.success(request, 'Receita Criada com Sucesso!')
            return redirect(reverse('authors:CreateRecipeDashboard'))
            
        else:
            messages.error(request, 'Erro! Tente Novamente.')
            print(form.errors)
        
    context = {
        'forms': form,
    }    
    
    return render(request, 'authors/pages/dash_board_create.html', context=context)
    
    
def dashboard_delete(request, id):
    recipe = get_object_or_404(RecipesModels, id=id, author=request.user)
    
    if str(request.method) == 'POST':
        recipe.delete()
        
        messages.success(request, 'Receita Apagada com Sucesso')
        return redirect(reverse('authors:dashboard'))
    
def profile(request):
    return render(request, 'authors/pages/profile.html')