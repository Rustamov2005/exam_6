from django.urls import path
from .views import shopdetail


urlpatterns = [
    path('shopdetail/', shopdetail, name='shopdetail'),
]