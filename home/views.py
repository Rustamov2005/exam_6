from django.shortcuts import render, redirect
from products.models import Fruits, Freeproducts, Organicvegetables
from .models import Users
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import auth


def home(request):
    fruites = Fruits.objects.all()
    if request.method == 'POST':
        search_query = request.POST.get('search', '')
        if search_query:
            organ = Fruits.objects.filter(name__icontains=search_query)
            if organ.exists():
                return render(request, 'index.html',
                              {'fruites': fruites, 'organ': organ, 'message': 'Successfully found'})
            else:
                return render(request, 'index.html', {'fruites': fruites, 'organ': organ, 'message': 'Not found'})
    freeproduct = Freeproducts.objects.all()
    organganic = Organicvegetables.objects.all()
    return render(request, 'index.html', {'fruites': fruites, 'freeproduct': freeproduct, 'organganic': organganic})


def users(request):
    users = Users.objects.all()
    return render(request, 'users.html', {'users': users})


def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password1 = request.POST['password1']
        except MultiValueDictKeyError:
            messages.info(request, 'Please provide both username and password')
            return redirect('home')
        user = auth.authenticate(username=username, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'auth/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,  first_name=first_name,  last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request, "Password don't match!")
            return redirect('register')
    else:
        return render(request, "auth/regester.html")
