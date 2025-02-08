from django.urls import path
from . import views

# URL DA APLICACAO

urlpatterns = [
    path('', views.MyView, name='home'),
    path('login/', views.login, name='login'),
    path('recipes/<int:id>/', views.recipes),
]
