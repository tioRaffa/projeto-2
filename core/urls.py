from django.urls import path
from .views import MyView, login

# URL DA APLICACAO

urlpatterns = [
    path('', MyView, name='home'),
    path('login/', login, name='login'),
]
