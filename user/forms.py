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

class WithdrawalForm(forms.Form):
    amount = forms.IntField(
        label = "amount",
        max_length = 9
    )

class TransferForm(forms.Form):
    account_num = forms.CharField(
        label = 'Account Number',
        max_length = 10
    )
    amount = forms.IntegerField(
        label = 'Amount'
    )