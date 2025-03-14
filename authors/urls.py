from django.urls import path
from authors import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'authors'

urlpatterns = [
    path('register/', views.register_view, name='RegisterView'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('perfil/<int:id>', views.Profile.as_view(), name='profile'),
    path('dashboard/', views.dashboard_user, name='dashboard'),
    path('dashboard/edition/<int:id>/', views.DashBoardRecipeEdit.as_view(), name='dashboard_edition'),
    path('create/recipes/', views.DashBoardCreate.as_view(), name='CreateRecipeDashboard'),
    path('dashboard/delete/<int:id>', views.DashBoardDelete.as_view(), name='dashboard_delete')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)