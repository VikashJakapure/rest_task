"""Ecolibrium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from firstapp import views
from django.contrib import admin
from firstapp.views import IndexView
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from firstapp.views import MovieRetrieveUpdateDestroyAPIView

from firstapp.views import UserCreateView,MoviesCreate

urlpatterns = [
# previous login view
# path('login/', views.user_login, name='login'),
    path('admin/', admin.site.urls),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/',UserCreateView.as_view()),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('', views.dashboard, name='dashboard'),
    path('api/',IndexView.as_view()),
    path('addmovie/', MoviesCreate.as_view()),

    path('api/<int:id>/',MovieRetrieveUpdateDestroyAPIView.as_view()),
    path('auth-jwt/', obtain_jwt_token),   #for JWT concept
    path('auth-jwt-refresh/', refresh_jwt_token), #for JWT concept
    path('auth-jwt-verify/', verify_jwt_token),  #for JWT concept
    # path('com/',Command.as_view()),

    

]