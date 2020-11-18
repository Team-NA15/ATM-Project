from django.shortcuts import render
from ..forms import ModCardForm
from user.models import ATMCard
from main.services import renderPage, getCardholderByNumber, setContextMessage

#Request to activate an ATM card
def activateATMCard(request): 
    renderData = {
        'request': request,
        'path': 'administrator/activate-atm-card.html',
        'context': { 
            'form': ModCardForm(),
            'message': '',
        } 
    }
    if request.method == 'POST': 
        form = ModCardForm(request.POST)
        if form.is_valid():
            #verify card holder exists, if card is string we have an error message 
            card = getCardholderByNumber(form.cleaned_data['card_number'])
            if not card: 
                setContextMessage(renderData['context'], card)
                return renderPage(renderData)

            if card.card_status == 'active': 
                setContextMessage(renderData['context'],'Card is already active')
                return renderPage(renderData)
            else: 
                card.card_status = 'active'
                card.save()
                setContextMessage(renderData['context'],'Card activated')
                return renderPage(renderData)
                
        else: 
            renderData['context']['message'] = 'Form is invalid'
            return renderPage(renderData)
    else: 
        return renderPage(renderData)
