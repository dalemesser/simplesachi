from django import forms
from . models import  Passenger,Airport


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = [
            'code',
            'city'
        ]

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = [
            'first_name',
            "last_name"
        ]

class UserForm(forms.Form):
    first_name= forms.CharField(max_length=256)
    password = forms.CharField(widget=forms.PasswordInput())

