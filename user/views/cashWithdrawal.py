from ..decorator import user_authenticated
from django.shortcuts import render 
from django.http import HttpResponse
from user.models import ATMCard
from ..forms import WithdrawalForm

#GET request to load page with form for withdrawing money 
@user_authenticated
def cashWithdrawal(request): 
    #logic for loading page for money withdrawal 
    if (request.method == 'POST'):
        try:
            card = ATMCard.objects.get(card_number = request.session['token'])
        except:
            print("Error with card number")
        account = card.account_number
        form = WithdrawalForm(request.POST)
        #Link frontend "amount entered" to withdrawal var
        withdrawal = 0.0
        #Update Database
        print('Money dispursed. New Balance: ', account.balance - withdrawal)
        return HttpResponse(account.balance)
    else:
        form = WithdrawalForm()
        return render(request, 'user/cardholder-login.html', {'form': form})