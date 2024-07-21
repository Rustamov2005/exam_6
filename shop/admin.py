from django.contrib import admin
from .models import Shopvegetable
from import_export.admin import ImportExportModelAdmin


@admin.register(Shopvegetable)
class ShopvegetableAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'rating', 'newprice', 'oldprice', 'img')
