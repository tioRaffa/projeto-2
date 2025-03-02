from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Digite sua Senha', 'required': 'True'}),
        error_messages={'required': 'Password must not be empty'}
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Confirme sua Senha', 'required': 'True'}),
        label="Confirme sua senha"
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
        
    def clean_password(self):
        data_pass1 = self.cleaned_data.get('password')
        data_pass2 = self.cleaned_data.get('password2')
        
        if 'senha' in data_pass1:
            raise ValidationError(
                'Serio? lkkkk',
                code='invalid',
            )
        
        
