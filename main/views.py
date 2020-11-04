from django.http import HttpResponse
from django.shortcuts import render 
from administrator.models import ATMachine

#Request that loads the ATM main home page 
def index(request):
    try: 
        machine = ATMachine.objects.get(atm_machine_uid = '1111222233334444')
    except: 
        return HttpResponse('Machine Error')

    if 'machine' not in request.session: 
        request.session['machine'] = machine.atm_machine_uid
    
    return render(request, 'main/home.html')


#HARDCODED ATM MACHINE
    #     machine = ATMachine(
    #     atm_machine_uid = '1111222233334444', 
    #     current_balance = 9999999999,
    #     location = '123 firefox lane', 
    #     minimum_balance = 100000, 
    #     last_refill_date = '2020-10-03', 
    #     next_maint_date = '2023-10-03'
    # )

    # machine.save()
    # print(ATMachine.objects.all())
