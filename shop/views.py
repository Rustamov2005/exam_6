from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Fruits, Shopvegetable

class ShopView(TemplateView):
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fruit'] = Fruits.objects.all()
        context['shop_vegetable'] = Shopvegetable.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        search = request.POST.get("search", "")
        shopp = Fruits.objects.filter(title__icontains=search)
        context = self.get_context_data()
        context['shopp'] = shopp
        return render(request, self.template_name, context)
