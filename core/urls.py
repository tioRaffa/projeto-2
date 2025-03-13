from django.urls import path
from . import views
from django.conf.urls import handler404
# URL DA APLICACAO



urlpatterns = [
    path('', views.RecipeListViewBase.as_view(), name='recipes_home'),
    path('recipes/search/', views.Search.as_view(), name='search_box'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail_page'),
    path('recipes/category/<int:pk>/',
         views.Category.as_view(), name='category'),
    path('skull/', views.skull),
    path('theory/', views.theory, name='theory')
]

handler404 = views.custom_404
