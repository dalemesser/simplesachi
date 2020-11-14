from django import forms
from . models import Learn

class LearnForm(forms.ModelForm):
    class Meta:
        model = Learn
        fields = '__all__'

class DateForm(forms.Form):
    date = forms.DateField()