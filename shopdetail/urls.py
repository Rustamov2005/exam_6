from django.urls import path
from .views import ShopDetailView

urlpatterns = [
    path('shopdetail/', ShopDetailView.as_view(), name='shopdetail'),
]
