from django.urls import path
from .views import allproducts, meats, fruits, breads, vegetables


urlpatterns = [
    path('allproducts/', allproducts, name='allproducts'),
    path('meat/', meats, name='meats'),
    path('fruits/', fruits, name='fruits'),
    path('breads/', breads, name='breads'),
    path('vegetables/', vegetables, name='vegetables'),
]
