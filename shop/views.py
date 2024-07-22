from django.shortcuts import render
from products.models import Fruits
from .models import Shopvegetable
from django.contrib.auth.decorators import login_required


@login_required
def shop(request):
    fruit = Fruits.objects.all()
    shop_vegetable = Shopvegetable.objects.all()
    return render(request, 'shop.html', {'fruit': fruit, 'shop_vegetable': shop_vegetable})
