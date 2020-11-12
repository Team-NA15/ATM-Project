from django import forms

class ModCardForm(forms.Form): 
    card_number = forms.CharField(
        label = 'Card Number', 
        max_length = 16
    )