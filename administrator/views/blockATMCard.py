from django.shortcuts import render
from user.models import ATMCard
from ..forms import ModCardForm 


#Request to block an ATM card
def blockATMCard(request): 
    if request.method == 'POST':
        form = ModCardForm(request.POST)
        if form.is_valid(): 
            try: 
                card = ATMCard.objects.get(card_number = form.cleaned_data['card_number'])
            except: 
                form = ModCardForm()
                return render(request, 'administrator/block-atm-card.html', {
                    'form': form, 
                    'message': 'Invalid Card Number'
                })
            form = ModCardForm()
            if card.card_status == 'active': 
                card.card_status = 'deactivated'
                card.save()
                return render(request, 'administrator/block-atm-card.html', {
                    'form': form, 
                    'message': 'Card has been blocked'
                })
            else: 
                return render(request, 'administrator/block-atm-card.html', {
                    'form': form, 
                    'message': 'Card already deactivated'
                })
        else: 
            form = ModCardForm()
            return render(request, 'administrator/block-atm-card.html', {
                'form': form, 
                'message': 'Form is invalid'
            })
    else: 
        form = ModCardForm()
        return render(request, 'administrator/block-atm-card.html', {
            'form': form
        })