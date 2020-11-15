from django import forms

<<<<<<< HEAD
class AdminForm(forms.Form): 
    card_number = forms.CharField(
        label = 'card number',
        max_length = 16
    )
    pin = forms.CharField(
        label = 'PIN', 
        max_length = 4
=======
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
>>>>>>> a233bbb1fa45df17a80b73acb433faac1c12e268
    )