from django.shortcuts import render
from .models import Cardpage, Cards
from django.contrib.auth.decorators import login_required


@login_required
def cart(request):
    cardpages = Cardpage.objects.all()
    cards = Cards.objects.all()
    return render(request, 'cart.html', {'cardpages': cardpages, 'cards': cards})


@login_required
def chackout(request):
    return render(request, 'chackout.html')


@login_required
def testimonial(request):
    return render(request, 'testimonial.html')


@login_required
def errorsl(request):
    return render(request, '404.html')
