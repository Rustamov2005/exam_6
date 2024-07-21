from django.shortcuts import render
from .models import Cardpage, Cards


def cart(request):
    cardpages = Cardpage.objects.all()
    cards = Cards.objects.all()
    return render(request, 'cart.html', {'cardpages': cardpages, 'cards': cards})


def chackout(request):
    return render(request, 'chackout.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def errorsl(request):
    return render(request, '404.html')
