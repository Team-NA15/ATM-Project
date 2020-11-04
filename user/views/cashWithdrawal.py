from ..decorator import user_authenticated
from django.shortcuts import render 
from django.http import HttpResponse
from user.models import ATMCard
from ..forms import WithdarawalForm

#GET request to load page with form for withdrawing money 
@user_authenticated
def cashWithdrawal(request): 
    #logic for loading page for money withdrawal 
    if (request.method == 'POST'):
        try:
            card = ATMCard.objects.get(card_number = request.session['token'])
        except:
            print("card not valid")
        account = card.account_number
        form = WithdarawalForm(request.POST)
        #Link frontend "amount entered" to amount var
        #Update Database
        print('Money dispursed. New Balance: ', account.balance - amount)
        return HttpResponse(account.balance)
    else:
        form = WithdarawalForm()
        return render(request, 'user/cardholder-login.html', {'form': form})