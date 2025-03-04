from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForms
from django.contrib import messages
import time


def register_view(request):
    
    
    if str(request.method) == 'POST':
        form = RegisterForm(request.POST or None)
        
        if form.is_valid():
            user = form.save(commit=False)
            # user.set_password(user.password)
            # user.save()
            
            form = RegisterForm()
            messages.success(request, 'Registro Concluido Com Sucesso')
        
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
            
            user = authenticate(
                username=username,
                password=password,
            )
            
            if user is not None:
                login(request, user)
                return redirect('recipes_home')
            
            else:
                messages.error(request, 'Erro! Digite a senha novamente')            

    
    
    context = {
        'form': form
    }
    
    return render(request, 'authors/pages/login.html', context=context)