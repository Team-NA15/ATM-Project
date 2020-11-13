from django.shortcuts import render
from user.models import ATMCard
from ..forms import ModCardForm 
from main.services import renderPage


#Request to block an ATM card
def blockATMCard(request):
    renderData = {
        'request': request,
        'path': 'administrator/block-atm-card.html',
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
                card.card_status = 'deactivated'
                card.save()
                renderData['context']['message'] = 'Card deactivated'
                return renderPage(renderData)
            else: 
                renderData['context']['message'] = 'Card already deactivated'
                return renderPage(renderData)
        else: 
            renderData['context']['message'] = 'Form is invalid'
            return renderPage(renderData)
    else: 
        return renderPage(renderData)