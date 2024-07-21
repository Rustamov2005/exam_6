from django import forms
from .models import Organicvegetables


class OrganicvegetablesForm(forms.ModelForm):
    class Meta:
        model = Organicvegetables
        fields = ['title']
