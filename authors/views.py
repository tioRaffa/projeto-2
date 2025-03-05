from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from .forms import RegisterForm, LoginForms
from django.contrib import messages
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
    
    # if str(request.method) != 'POST':
    #     return redirect(reverse('authors:login'))
    
    # if request.POST.get('username') != request.user.username:
    #     return redirect(reverse('authors:login'))
        
    
    logout(request)
    return redirect(reverse('recipes_home'))

@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_user(request):
    return render(request, 'authors/pages/dash_board.html')