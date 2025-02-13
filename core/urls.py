from django.urls import path
from . import views

# URL DA APLICACAO

urlpatterns = [
    path('', views.MyView, name='recipes_home'),
    path('login/', views.login, name='login'),
    path('recipes/<int:id>/', views.recipes, name='recipe_detail_page'),
    path('recipes/category/<int:id>/',
         views.category, name='category'),
]
