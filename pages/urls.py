from django.urls import path
from .views import cart, chackout, testimonial, errorsl


urlpatterns = [
    path('cart/', cart, name='cart'),
    path('chackout/', chackout, name='chackout'),
    path('testimonial/', testimonial, name='testimonial'),
    path('errors/', errorsl, name='errors'),
]