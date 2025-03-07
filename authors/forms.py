from django import forms
from utils.authors.django_forms import strong_password
from django.contrib.auth.models import User
from core.models import RecipesModels, Category
from collections import defaultdict
from django.core.exceptions import ValidationError

import re


txt = 'ex: Ab12345678'
class RegisterForm(forms.ModelForm):
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': f'{txt}', 'required': 'True'}),
        validators=[strong_password]
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Confirme sua Senha', 'required': 'True'}),
    )
    username = forms.CharField(
        max_length=50,
        min_length=2,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input-box',
            'placeholder': 'Digite seu Nome de Usuário',
        })
    )
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Digite seu Nome', 'required': 'True'}),
            'last_name': forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Digite seu Último Nome','required': 'True'}),
            'email': forms.EmailInput(attrs={'class': 'input-box', 'placeholder': 'ex: exemploemail@gmail.com','required': 'True'}),
        }
        
    def clean_email(self):
        data_email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=data_email).exists()
        
        if exists:
            raise ValidationError(
                'E-mail ja cadastrado'
            )
    
    
    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')
        
        if data[0].islower():
            raise ValidationError('A primeira letra deve ser Maiscula')

        return data
       
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        
        
        if password != password2:
            raise ValidationError('Erro na confirmaçao, Digite Novamente!')
        

class LoginForms(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input100',
            'placeholder': 'Digite o nome de usuário'
        })
    )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput({
        'class': 'input100',
        'type': 'password',
        'placeholder': 'Digite sua Senha'
    }))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        data = User.objects.filter(username=username).exists()
        
        if not data:
            raise ValidationError(
                'Usuario nao encontrado!'
            )
        return username
    
    
class AuthorRecipeForm(forms.ModelForm):
    
    class Meta:
        model = RecipesModels
        fields = [
            'title', 'description', 'preparation_time',
            'preparation_time_unit', 'servings',
            'servings_unit', 'preparation_steps',
            'cover',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'type': 'text', 'class': 'form_input','id': 'nome', 'placeholder': 'Nome da Receita', }),
            'preparation_time': forms.NumberInput(attrs={'min': 1, 'step': 1, 'class': 'form_input', 'placeholder': 'Tempo de Preparação'}),
            'servings': forms.NumberInput(attrs={'min': 1, 'step': 1, 'class': 'form_input', 'placeholder': 'Serve Quantos?'}),
            'servings_unit': forms.TextInput(attrs={'type': 'text', 'class': 'form_input','id': 'nome', 'placeholder': 'Porcao', }),
            'preparation_steps': forms.Textarea(attrs={'name': 'mensagem', 'id': 'message', 'cols': '30', 'rows': '3', 'class': 'form_input message_input', 'style': 'background-color: rgb(149, 137, 137, 0.2);'}),
            'description': forms.Textarea(attrs={'name': 'mensagem', 'id': 'message', 'cols': '30', 'rows': '3', 'class': 'form_input message_input', 'style': 'background-color: rgb(149, 137, 137, 0.2);'}),
            'cover': forms.FileInput(),
            'preparation_time_unit': forms.Select(attrs={'type': 'text', 'class': 'form_input','id': 'nome'}, choices=(('Minutos', 'Minutos'), ('Horas', 'Horas'))),
            'category': forms.Select(attrs={'type': 'text', 'class': 'form_input','id': 'nome'} ),
        }


class AuthorCreateRecipe(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self._my_errors = defaultdict(list)
        
    class Meta:
        model = RecipesModels
        fields = [
            'title', 'description', 'preparation_time',
            'preparation_time_unit', 'servings',
            'servings_unit', 'preparation_steps',
            'cover', 'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'type': 'text', 'class': 'form_input','id': 'nome', 'placeholder': 'Nome da Receita', }),
            'preparation_time': forms.NumberInput(attrs={'min': 1, 'step': 1, 'class': 'form_input', 'placeholder': 'Tempo de Preparação'}),
            'servings': forms.NumberInput(attrs={'min': 1, 'step': 1, 'class': 'form_input', 'placeholder': 'Serve Quantos?'}),
            'servings_unit': forms.TextInput(attrs={'type': 'text', 'class': 'form_input','id': 'nome', 'placeholder': 'Porcao', }),
            'preparation_steps': forms.Textarea(attrs={'name': 'mensagem', 'id': 'message', 'cols': '30', 'rows': '3', 'class': 'form_input message_input', 'style': 'background-color: rgb(149, 137, 137, 0.2);'}),
            'description': forms.Textarea(attrs={'name': 'mensagem', 'id': 'message', 'cols': '30', 'rows': '3', 'class': 'form_input message_input', 'style': 'background-color: rgb(149, 137, 137, 0.2);'}),
            'cover': forms.FileInput(),
            'preparation_time_unit': forms.Select(attrs={'type': 'text', 'class': 'form_input','id': 'nome'}, choices=(('Minutos', 'Minutos'), ('Horas', 'Horas'))),
        }
        
        category = forms.ModelChoiceField(
            queryset=Category.objects.all(),
            required=True,
            widget=forms.Select(attrs={'type': 'text', 'class': 'form_input','id': 'nome'})
        )
        
    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        
        title = self.cleaned_data.get('title')
        
        
        return super_clean