from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('', views.home_redirect),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]