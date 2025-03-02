from django.urls import path
from . import views
from django.conf.urls import handler404
# URL DA APLICACAO

urlpatterns = [
    path('', views.MyView, name='recipes_home'),
    path('recipes/search/', views.search, name='search_box'),
    path('recipes/<int:id>/', views.recipes, name='recipe_detail_page'),
    path('recipes/category/<int:id>/',
         views.category, name='category')
]

handler404 = views.custom_404
