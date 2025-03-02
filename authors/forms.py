from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Digite sua Senha', 'required': 'True'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Confirme sua Senha', 'required': 'True'}),
    )
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Digite seu Nome', 'required': 'True'}),
            'last_name': forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Digite seu Último Nome','required': 'True'}),
            'username': forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Digite seu Nome de Usuário','required': 'True'}),
            'email': forms.EmailInput(attrs={'class': 'input-box', 'placeholder': 'ex: exemploemail@gmail.com','required': 'True'}),
        }
        
        
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        
        print(password, password2)
        
        if password != password2:
            raise ValidationError('erro')