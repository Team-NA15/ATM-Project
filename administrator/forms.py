from django import forms

class BlockCardForm(forms.Form): 
    card_number = forms.CharField(
        label = 'Card Number', 
        max_length = 16
    )