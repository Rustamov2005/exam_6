from django import forms
from .models import Cards


class CardsForm(forms.ModelForm):
    class Meta:
        model = Cards
        fields = ['subtotal', 'total_price', 'total', 'shipping', 'cardnumber', 'users']
