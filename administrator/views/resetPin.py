from django.shortcuts import render
from ..forms import ModCardForm
from user.models import ATMCard
from random import randint

#Request to reset PIN so the user can use their card
def resetPin(request):
    if request.method == 'POST': 
        form = ModCardForm(request.POST)
        if form.is_valid():
            try: 
                card = ATMCard.objects.get(card_number = form.cleaned_data['card_number'])
            except: 
                form = ModCardForm()
                return render(request, 'administrator/reset-pin.html', {
                    'form': form, 
                    'message': 'Card is invalid'
                })
            form = ModCardForm()
            card.pin = str(randint(1000, 9999))
            card.save()
            return render(request, 'administrator/reset-pin.html', {
                'form': form, 
                'message': 'PIN has been reset to ' + card.pin
            })
        else: 
            form = ModCardForm()
            return render(request, 'administrator/reset-pin.html', {
                'form': form, 
                'message': 'Form is not valid'
            })
    else: 
        form = ModCardForm()
        return render(request, 'administrator/reset-pin.html', {
            'form': form
        })
    return