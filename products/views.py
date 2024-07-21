from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Allproducts, Meat, Fruits, Breads


def allproducts(request):
    allproducts = Allproducts.objects.all()
    meat = Meat.objects.all()
    fruits = Fruits.objects.all()
    breads = Breads.objects.all()
    return render(request, 'allproducte.html', {'allproducts': allproducts, 'meat': meat, 'fruits': fruits, 'breads': breads})


def meats(request):
    meats = Meat.objects.all()
    return render(request, 'meat.html', {'meats': meats})


def fruits(request):
    fruits = Fruits.objects.all()
    return render(request, 'fruits.html', {'fruits': fruits})


def breads(request):
    breads = Breads.objects.all()
    return render(request, 'breads.html', {'breads': breads})


def vegetables(request):
    vegetables = Allproducts.objects.all()
    return render(request, 'vegetables.html', {'vegetables': vegetables})
