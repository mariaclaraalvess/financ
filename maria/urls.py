from django.contrib import admin
from django.urls import path
from financem import views
from financem.views import login_view, register_view, profile_view, home_view
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Rota vazia para a visualização de login
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('app/', views.home_view, name='app'),
]
