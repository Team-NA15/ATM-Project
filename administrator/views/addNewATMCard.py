from django.shortcuts import render, redirect
from administrator.models import ATMachine
from ..forms import AdminForm, newCardForm
from user.models import ATMCard, AccountExtension
from ..decorator import admin_authenticated

#Request to load page with form to add new ATM Card
@admin_authenticated
def addNewATMCard(request): 

    if request.method == 'POST': 
        form = newCardForm(request.POST)
        if form.is_valid():
                try: 
                    card = ATMCard.objects.get(card_number = form.cleaned_data['card_number'])
                    form = newCardForm()
                    return render(request, 'administrator/add-atm-card.html', {'form': form, 'message': 'Already a card with that number'})
                except:
                    print("Card is good")
                try:
                    account = AccountExtension.objects.get(account_number = form.cleaned_data['account_number'])
                    #account = AccountExtension.objects.get(account_number = '1111111111')
                except:
                    print (form.cleaned_data['account_number'])
                    form = newCardForm()
                    return render(request, 'administrator/add-atm-card.html', {'form': form, 'message': 'Not a valid account number'})
                #if card.card_number == form.cleaned_data['card_number']: 
                newATMCard = ATMCard(
                    card_number = form.cleaned_data['card_number'],
                    pin = form.cleaned_data['pin'],
                    name = form.cleaned_data['name'], 
                    address = form.cleaned_data['address'], 
                    phone_number = form.cleaned_data['phone_number']
                )
                newATMCard.account_number = account
                newATMCard.save()
                form = newCardForm()
                return render(request, 'administrator/add-atm-card.html', {'form': form, 'message': 'Card created succesfully!'})
            #else: 
                #request.session['token'] = card.card_number
                #return redirect('/administrator')
        else: 
            return render(request, 'administrator/add-atm-card.html', {'form': form, 'message': 'Form not valid'})
    else:
        print(AccountExtension.objects.all())
        form = newCardForm()
        return render(request, 'administrator/add-atm-card.html', {'form': form})