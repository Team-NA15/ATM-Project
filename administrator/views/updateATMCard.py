from django.shortcuts import render 

#Request to load page for update ATM card options 
def updateATMCard(request): 
    #logic for loading page with update options for ATM card goes here 
    
    return render(request, 'administrator/update-atm-card.html')
