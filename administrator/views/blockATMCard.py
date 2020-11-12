from django.shortcuts import render
from user.models import ATMCard
from ..forms import BlockCardForm 


#Request to block an ATM card
def blockATMCard(request): 
    if request.method == 'POST':
        form = BlockCardForm(request.POST)
        if form.is_valid(): 
            try: 
                card = ATMCard.objects.get(card_number = form.cleaned_data['card_number'])
            except: 
                form = BlockCardForm()
                return render(request, 'administrator/block-atm-card.html', {
                    'form': form, 
                    'message': 'Invalid Card Number'
                })
            form = BlockCardForm()
            if card.card_status == 'active': 
                card.card_status = 'deactivated'
                card.save()
            else: 
                return render(request, 'administrator/block-atm-card.html', {
                    'form': form, 
                    'message': 'Card already deactivated'
                })
            return render(request, 'administrator/block-atm-card.html', {
                'form': form, 
                'message': 'Card has been blocked'
            })
    else: 
        form = BlockCardForm()
        return render(request, 'administrator/block-atm-card.html', {
            'form': form
        })