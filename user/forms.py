from django import forms

class UserForm(forms.Form): 
    card_number = forms.CharField(
        label = 'card number',
        max_length = 16
    )
    pin = forms.CharField(
        label = 'PIN', 
        max_length = 4
    )

class WithdarawalForm(forms.Form):
    card_number = forms.CharField(
        label = 'card number',
        max_length = 16
    )
    amount = forms.FloatField(
        label = 'amount',
        max_length = 7
    )