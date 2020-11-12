from ..decorator import user_authenticated
from django.shortcuts import render, redirect
from user.models import ATMCard
from ..forms import WithdrawalForm
from main.models import Transaction
from administrator.models import ATMachine
import time

#GET request to load page with form for withdrawing money 
@user_authenticated
def cashWithdrawal(request): 
    #logic for loading page for money withdrawal 
    if (request.method == 'POST'):
        try:
            card = ATMCard.objects.get(card_number = request.session['token'])
        except:
            print("Error with card number")
        form = WithdrawalForm()
        amount = form.cleaned_data['amount']
        ## checks our balance 
        if card.account_number.balance < amount:
            ## if there are not enough funds 
            form = WithdrawalForm()
            return render(request, 'user/cash-withdrawal.html', {
                'form': form,
                'message': 'Insufficient Funds.'
            })
        else: 
            # there are enough funds   
            account = card.account_number
            form = WithdrawalForm(request.POST)
            #Update Database
            print('Money dispursed. New Balance: ', account.balance - amount)
            card.account_number.save()
            transaction = Transaction(
                status = 'complete',
                response_code = '200',
                transaction_type = 'cash-withdraw'
            )
            transaction.atm_card_number = card
            machine = ATMachine.objects.get(atm_machine_uid = request.session['machine'])
            transaction.atm_machine_uid = machine
            transaction.save()
            form = WithdrawalForm()
            return render(request, 'user/cash-withdrawal.html', {
                'message': 'Funds Withdrawn Successfully',
                'form': form
            })
    else:
        form = WithdrawalForm()
        return render(request, 'user/cardholder-login.html', {'form': form})