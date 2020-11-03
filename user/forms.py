from django import forms

class UserForm(forms.Form): 
    card_number = forms.CharField(
        max_length = 16
    )
    pin = forms.CharField(
        max_length = 4
    )