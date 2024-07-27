from django.views.generic import TemplateView
from .models import Cardpage, Cards

class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cardpages'] = Cardpage.objects.all()
        context['cards'] = Cards.objects.all()
        return context