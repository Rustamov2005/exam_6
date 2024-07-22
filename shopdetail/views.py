from django.shortcuts import render
from shop.models import Shopvegetable
from .models import Maxsulot, Related
from home.models import Comments
from django.contrib.auth.decorators import login_required


@login_required
def shopdetail(request):
    shopdetail = Shopvegetable.objects.all()
    maxsulot = Maxsulot.objects.all()
    related = Related.objects.all()
    comments = Comments.objects.all()
    return render(request, 'shop-detail.html', {'shopdetail': shopdetail, 'maxsulot': maxsulot, 'related': related, 'comments': comments})
