from django.urls import path
from .views import MyView, contato, sobre

# URL DA APLICACAO

urlpatterns = [
    path('', MyView, name='home'),
    path('contato/', contato, name='contato'),
    path('sobre/', sobre, name='sobre')
]
