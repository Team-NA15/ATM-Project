from django.shortcuts import render, redirect
from administrator.models import ATMachine
from ..forms import AdminForm
from user.models import ATMCard
#Request to load page with form to add new ATM Card
def addNewATMCard(request): 
    #logic to load page for adding new ATM Card
    #form = AdminForm()
    #return render(request, 'administrator/add-atm-card.html', {'form': form})
    #if request.method == 'GET': 
     #   form = AdminForm(request.GET)
      #  if form.is_valid():
       #      form = AdminForm()
        
        #return render(request, 'administrator/add-atm-card.html', {'form': form})
    if request.method == 'POST': 
        form = AdminForm(request.POST)
        if form.is_valid():
            try: 
                card = ATMCard.objects.get(card_number = form.cleaned_data['card_number'])
            except: 
                return render(request, 'administrator/add-atm-card.html', {'form': form, 'message': 'Not a valid card number'})
            
            if card.card_number == form.cleaned_data['card_number']: 
                return render(request, 'administrator/add-atm-card.html', {'form': form, 'message': 'Already a card with that number'})
            #else: 
                #request.session['token'] = card.card_number
                #return redirect('/administrator')
        else: 
            return render(request, 'administrator/add-atm-card.html', {'form': form, 'message': 'Form not valid'})
    else:
        form = AdminForm()
        return render(request, 'administrator/add-atm-card.html', {'form': form})