from django.urls import path
from .views import home, users, login, register


urlpatterns = [
    path('', home, name='home'),
    path('users/', users, name='users'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]