from django.shortcuts import render
from ..forms import ModCardForm
from user.models import ATMCard
from random import randint
from main.services import renderPage

#Request to reset PIN so the user can use their card
def resetPin(request):
    renderData = {
        'request': request,
        'path': 'administrator/reset-pin.html',
        'context': { 
            'form': ModCardForm(),
            'message': '',
        } 
    }
    if request.method == 'POST': 
        form = ModCardForm(request.POST)
        if form.is_valid():
            try: 
                card = ATMCard.objects.get(card_number = form.cleaned_data['card_number'])
            except: 
                renderData['context']['message'] = 'Card Number Invalid'
                return renderPage(renderData)

            card.pin = str(randint(1000, 9999))
            card.save()
            renderData['context']['message'] = 'PIN has been reset to ' + card.pin
            return renderPage(renderData)

        else: 
            renderData['context']['message'] = 'Form is invalid'
            return renderPage(renderData)
    else: 
        return renderPage(renderData)
    