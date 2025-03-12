from django.urls import path
from . import views
from django.conf.urls import handler404
# URL DA APLICACAO



urlpatterns = [
    path('', views.RecipeListViewBase.as_view(), name='recipes_home'),
    path('recipes/search/', views.Search.as_view(), name='search_box'),
    path('recipes/<int:id>/', views.recipes, name='recipe_detail_page'),
    path('recipes/category/<int:id>/',
         views.Category.as_view(), name='category'),
    path('skull/', views.skull)
]

handler404 = views.custom_404
