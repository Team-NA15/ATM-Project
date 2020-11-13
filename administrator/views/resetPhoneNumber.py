from django.shortcuts import render
from ..forms import PhoneResetForm
from user.models import ATMCard
from main.services import renderPage
import re

#Request to reset phone number
def resetPhoneNumber(request): 
    renderData = {
        'request': request,
        'path': 'administrator/reset-phone-number.html',
        'context': { 
            'form': PhoneResetForm(),
            'message': '',
        } 
    }
    if request.method == 'POST': 
        form = PhoneResetForm(request.POST)
        
        if form.is_valid():
            try: 
                card = ATMCard.objects.get(card_number = form.cleaned_data['card_number'])
            except: 
                renderData['context']['message'] = 'Card Number Invalid'
                return renderPage(renderData)

            check = form.cleaned_data['phone_number'].replace('-', '')
            if (check.isdigit()):
                print(form.cleaned_data['phone_number'])
                card.phone_number = form.cleaned_data['phone_number']
                card.save()
                renderData['context']['message'] = 'Phone Number changed to ' + card.phone_number
                return renderPage(renderData)               

            else:
                renderData['context']['message'] = 'Invalid Phone Number'
                return renderPage(renderData)

    else: 
        return renderPage(renderData) 