from django.shortcuts import render
from user.models import ATMCard
from ..forms import BlockATMCardForm 


#Request to block an ATM card
def blockATMCard(request): 
    if request.method == 'POST':
        print('post')
    else: 
        form = BlockATMCardForm()
        return render(request, 'administrator/block-atm-card.html', {
            'form': form
        })