from django.shortcuts import render
from ..forms import ModCardForm
from user.models import ATMCard
from random import randint
from main.services import renderPage, getCardholderByNumber, setContextMessage

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
            card = getCardholderByNumber(form.cleaned_data['card_number'])
            if isinstance(card, str): 
                setContextMessage(renderData['context'], card)
                return renderPage(renderData)

            card.pin = str(randint(1000, 9999))
            card.save()
            setContextMessage(renderData['context'], 'PIN has been reset to ' + card.pin)
            return renderPage(renderData)

        else: 
            setContextMessage(renderData['context'], 'Form is invalid')
            return renderPage(renderData)
    else: 
        return renderPage(renderData)
    