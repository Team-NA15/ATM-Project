from django.shortcuts import render, redirect
from ..forms import UserForm
from django.http import HttpResponse
from user.models import ATMCard, AccountExtension
from django.core import serializers
from random import randint
from ..decorator import user_authenticated


@user_authenticated
def cardholderLogin(request): 
    if request.method == 'POST': 
        form = UserForm(request.POST)
        if form.is_valid():
            try: 
                card = ATMCard.objects.get(card_number = form.cleaned_data['card_number'])
            except: 
                return render(request, 'user/cardholder-login.html', {'form': form, 'message': 'Not a valid card number'})
            
            if card.pin == form.cleaned_data['pin']: 
                request.session['token'] = card.card_number
                return redirect('/user')
            else: 
                return render(request, 'user/cardholder-login.html', {'form': form, 'message': 'Pin does not match'})
        else: 
            return render(request, 'user/cardholder-login.html', {'form': form, 'message': 'Form not valid'})
    else:
        form = UserForm()
        return render(request, 'user/cardholder-login.html', {'form': form})

#sample card number for testing: 1605104397380560