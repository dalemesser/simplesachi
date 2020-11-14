from django import forms
from . models import Wiwarana

class TypeForm(forms.ModelForm):
    class Meta:
        model = Wiwarana
        fields = [
            "year",
            "text",
            "number",
            "ansewer"
        ]
class YearForm(forms.ModelForm):
    class Meta:
        model = Wiwarana
        fields = [
            'year'
        ]