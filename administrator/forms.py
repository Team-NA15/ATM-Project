from django import forms

class ModCardStatusForm(forms.Form): 
    card_number = forms.CharField(
        label = 'Card Number', 
        max_length = 16
    )