from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('registration', views.registration, name='registration'),
    path('home', views.home, name='home'),
    path('main', views.main, name='main'),
    path('', views.login, name='home'),
]