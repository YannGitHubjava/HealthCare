from django import forms
from .models import Waste

class WasteForm(forms.Form):
    class Meta:
        model = Waste
        fields = '__all__'