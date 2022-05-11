from django import forms
from .models import AddressModel


class AddressModelForm(forms.ModelForm):
    class Meta:
        model = AddressModel
        fields = ['name']