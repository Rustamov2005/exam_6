from django.contrib.auth.views import LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from home.models import Fruits, Freeproducts, Organicvegetables


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fruites'] = Fruits.objects.all()
        context['freeproduct'] = Freeproducts.objects.all()
        context['organganic'] = Organicvegetables.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        search = request.POST.get("search", "")
        shopp = Fruits.objects.filter(title__icontains=search)
        context = self.get_context_data()
        context['shopp'] = shopp
        return render(request, self.template_name, context)


class UsersListView(ListView):
    model = Users
    template_name = 'users.html'
    context_object_name = 'users'


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'

    def form_valid(self, form):
        user = form.get_user()
        if user:
            messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Login failed. Please check your username and password.')
        return super().form_invalid(form)


class RegisterView(FormView):
    template_name = 'auth/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            form.add_error('username', 'Username Taken')
            return self.form_invalid(form)

        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        messages.success(self.request, 'User created successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Password don't match or username already taken!")
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = 'login'




