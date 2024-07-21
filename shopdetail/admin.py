from django.contrib import admin
from .models import Maxsulot, Related
from import_export.admin import ImportExportModelAdmin


@admin.register(Maxsulot)
class MaxsulotAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'rating', 'count', 'img')


@admin.register(Related)
class RelatedAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'img', 'price')
