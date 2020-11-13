from django.shortcuts import render
from ..forms import ModCardForm
from user.models import ATMCard
from main.services import renderPage

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
            try: 
                card = ATMCard.objects.get(card_number = form.cleaned_data['card_number'])
            except: 
                renderData['context']['message'] = 'Card Number Invalid'
                return renderPage(renderData)

            if card.card_status == 'active': 
                renderData['context']['message'] = 'Card is already active'
                return renderPage(renderData)
            else: 
                card.card_status = 'active'
                card.save()
                renderData['context']['message'] = 'Card activated'
                return renderPage(renderData)
                
        else: 
            renderData['context']['message'] = 'Form is invalid'
            return renderPage(renderData)
    else: 
        return renderPage(renderData)
