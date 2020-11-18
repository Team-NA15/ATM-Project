#Request to view status of ATM Machine
from django.shortcuts import render, redirect
from administrator.models import ATMachine
from ..forms import AdminForm
from user.models import ATMCard
from ..decorator import admin_authenticated

@admin_authenticated
def viewATMachineStatus(request): 
    #logic for viewing ATM machine status goes here 
    status = 'active'
    machID = 1111222233334444
    balance = 9999999999
    minBal = 1111111111
    address = '123 test this way'
    refill = '10/14/20'
    maintenance = '05/05/21'
    #ATMachine.objects.get(location = request.session['machine'])

    return render(request, 'administrator/atm-machine-status.html', {'status':status,'machID':machID, 'balance':balance, 'minBal':minBal, 'address': address, 'refill':refill, 'maintenance':maintenance})