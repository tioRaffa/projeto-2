from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages


def register_view(request):
    
    
    if str(request.method) == 'POST':
        form = RegisterForm(request.POST or None)
        
        if form.is_valid():
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


def login(request):
    return render(request, 'authors/pages/login.html')