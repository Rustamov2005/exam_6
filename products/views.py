from django.views.generic import TemplateView
from .models import Allproducts, Meat, Fruits, Breads

class AllProductsView(TemplateView):
    template_name = 'allproducte.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allproducts'] = Allproducts.objects.all()
        context['meat'] = Meat.objects.all()
        context['fruits'] = Fruits.objects.all()
        context['breads'] = Breads.objects.all()
        return context
