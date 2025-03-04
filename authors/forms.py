from django import forms
from utils.authors.django_forms import strong_password
from django.contrib.auth.models import User

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
    