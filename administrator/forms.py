from django import forms

class ModCardForm(forms.Form): 
    card_number = forms.CharField(
        label = 'Card Number', 
        max_length = 16
    )

class PhoneResetForm(forms.Form): 
    card_number = forms.CharField(
        label = 'Card Number', 
        max_length = 16
    )
    phone_number = forms.CharField(
        label = 'New Phone Number', 
        max_length = 12
    )