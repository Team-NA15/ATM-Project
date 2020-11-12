from django.shortcuts import render
from ..forms import ModCardForm
from user.models import ATMCard

#Request to activate an ATM card
def activateATMCard(request): 
    if request.method == 'POST': 
        form = ModCardForm(request.POST)
        if form.is_valid():
            try: 
                card = ATMCard.objects.get(card_number = form.cleaned_data['card_number'])
            except: 
                form = ModCardForm()
                return render(request, 'administrator/activate-atm-card.html', {
                    'form': form, 
                    'message': 'Card is invalid'
                })
            form = ModCardForm()
            if card.card_status == 'active': 
                return render(request, 'administrator/activate-atm-card.html', {
                    'form': form, 
                    'message': 'Card is already active'
                })
            else: 
                card.card_status = 'active'
                card.save()
                return render(request, 'administrator/activate-atm-card.html', {
                    'form': form, 
                    'message': 'Card has been activated'
                })
                
        else: 
            form = ModCardForm()
            return render(request, 'administrator/activate-atm-card.html', {
                'form': form, 
                'message': 'Form is invalid'
            })
    else: 
        print(request.path)
        form = ModCardForm()
        return render(request, 'administrator/activate-atm-card.html', {
            'form': form
        })
    return 