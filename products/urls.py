from django.urls import path
from .views import AllProductsView

urlpatterns = [
    path('allproducts/', AllProductsView.as_view(), name='allproducts'),
]
