from django.shortcuts import render
from ..forms import ModCardStatusForm
from user.models import ATMCard

#Request to activate an ATM card
def activateATMCard(request): 
    if request.method == 'POST': 
        form = ModCardStatusForm(request.POST)
        if form.is_valid():
            try: 
                card = ATMCard.objects.get(card_number = form.cleaned_data['card_number'])
            except: 
                form = ModCardStatusForm()
                return render(request, 'administrator/activate-atm-card.html', {
                    'form': form, 
                    'message': 'Card is invalid'
                })
            form = ModCardStatusForm()
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
            form = ModCardStatusForm()
            return render(request, 'administrator/activate-atm-card.html', {
                'form': form, 
                'message': 'Form is invalid'
            })
    else: 
        print(request.path)
        form = ModCardStatusForm()
        return render(request, 'administrator/activate-atm-card.html', {
            'form': form
        })
    return 