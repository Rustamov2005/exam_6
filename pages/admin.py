from django.contrib import admin
from .models import Cardpage, Cards
from import_export.admin import ImportExportModelAdmin


@admin.register(Cards)
class CardsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'subtotal', 'total_price', 'cardnumber')


@admin.register(Cardpage)
class CardpageAdmin(ImportExportModelAdmin):
    list_display = ('img', 'title', 'price', 'quantity', 'total_price', 'handle')


