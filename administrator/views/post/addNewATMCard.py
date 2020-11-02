from django.http import HttpResponse
from user.models import ATMCard, AccountExtension
from random import randint
from datetime import date 

def getExpireDate(date): 
    try: 
        return date.replace(year = date.year + 5)
    except ValueError: 
        return date + (date(date.year + 3, 1, 1) - date(date.year, 1, 1))


#POST request to add a new an ATM card
def addNewATMCard(request):
    #HARDCODED EXAMPLE 
    if request.method == 'POST': 
        card_num = randint(1000000000000000,9999999999999999)
        account = AccountExtension.objects.get(account_number = 1111111111)
        
        card = ATMCard(
            card_number = card_num,
            pin = 5555, 
            name = 'brandon corn', 
            date_issued = date.today(), 
            expire_date = getExpireDate(date.today()),
            address = '111 choochoo lane', 
            two_fact_auth_status = 'on', 
            phone_number = '111-2222', 
            card_status = 'deactivated'
        )
        # FOREIGN KEYS MUST BE SET AFTER THE CREATION OF THE OBJECT
        card.account_number = account.account_number
        print('card-number: ', card.card_number, '\naccount_number: ', card.account_number)
        # THEN WE CAN SAVE
        card.save()
        # HERE IS AN EXAMPLE OF RETRIEVING AN ATMCARD BY CARD NUMBER
        newCard = ATMCard.objects.get(card_number = 3887665486623486)
        print(newCard)
        return HttpResponse(card)
    return HttpResponse('An error occurred')