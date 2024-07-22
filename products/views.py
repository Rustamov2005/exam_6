from django.shortcuts import render
from .models import Allproducts, Meat, Fruits, Breads
from django.contrib.auth.decorators import login_required


@login_required
def allproducts(request):
    allproducts = Allproducts.objects.all()
    meat = Meat.objects.all()
    fruits = Fruits.objects.all()
    breads = Breads.objects.all()
    return render(request, 'allproducte.html', {'allproducts': allproducts, 'meat': meat, 'fruits': fruits, 'breads': breads})


@login_required
def meats(request):
    meats = Meat.objects.all()
    return render(request, 'meat.html', {'meats': meats})


@login_required
def fruits(request):
    fruits = Fruits.objects.all()
    return render(request, 'fruits.html', {'fruits': fruits})


@login_required
def breads(request):
    breads = Breads.objects.all()
    return render(request, 'breads.html', {'breads': breads})


@login_required
def vegetables(request):
    vegetables = Allproducts.objects.all()
    return render(request, 'vegetables.html', {'vegetables': vegetables})
