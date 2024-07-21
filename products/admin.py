from django.contrib import admin
from .models import Allproducts, Meat, Fruits, Breads, Freeproducts, Organicvegetables
from import_export.admin import ImportExportModelAdmin


@admin.register(Allproducts)
class AllproductsAdmin(ImportExportModelAdmin):
    list_display = ('title', 'price', 'img', 'description')


@admin.register(Meat)
class MeatAdmin(ImportExportModelAdmin):
    list_display = ('title', 'price', 'img', 'description')


@admin.register(Fruits)
class FruitsAdmin(ImportExportModelAdmin):
    list_display = ('title', 'price', 'img', 'description')


@admin.register(Breads)
class BreadsAdmin(ImportExportModelAdmin):
    list_display = ('title', 'price', 'img', 'description')


@admin.register(Organicvegetables)
class OrganicvegetablesAdmin(ImportExportModelAdmin):
    list_display = ('title', 'price', 'img', 'description')


@admin.register(Freeproducts)
class FreeproductsAdmin(ImportExportModelAdmin):
    list_display = ('title', 'price', 'img', 'description')
