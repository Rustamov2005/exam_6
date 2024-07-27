from django.views.generic import TemplateView
from .models import Shopvegetable, Maxsulot, Related, Comments

class ShopDetailView(TemplateView):
    template_name = 'shop-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shopdetail'] = Shopvegetable.objects.all()
        context['maxsulot'] = Maxsulot.objects.all()
        context['related'] = Related.objects.all()
        context['comments'] = Comments.objects.all()
        return context
