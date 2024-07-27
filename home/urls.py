from django.urls import path
from .views import CustomLogoutView, RegisterView, CustomLoginView, UsersListView


urlpatterns = [
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('users/', UsersListView.as_view(), name='users'),
]
