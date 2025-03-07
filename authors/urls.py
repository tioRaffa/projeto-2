from django.urls import path
from authors import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'authors'

urlpatterns = [
    path('register/', views.register_view, name='RegisterView'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard_user, name='dashboard'),
    path('dashboard/edition/<int:id>/', views.dashboard_edition, name='dashboard_edition'),
    path('create/recipes/', views.dashboard_create_recipe, name='CreateRecipeDashboard'),
    path('dashboard/delete/<int:id>', views.dashboard_delete, name='dashboard_delete')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)