from django.urls import path
from authors import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'authors'

urlpatterns = [
    path('register/', views.register_view, name='RegisterView'),
    path('login/', views.login, name='login'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)