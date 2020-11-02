from django.shortcuts import render 
from user.models import AccountExtension

#GET request loads page with options for ATM cardholder 
def home(request): 

    return render(request, 'user/home.html')


    #HARDCODED EXAMPLE OF MODEL CREATION
    # acc = AccountExtension(
    #     account_number = 2222222222,
    #     name = 'brandon corn', 
    #     phone_number = '569-1624', 
    #     balance = 9999999
    # )  
    # acc.save()
    # accounts = AccountExtension.objects.all()
    # AccountExtension.objects.all().delete()
    # for account in accounts: 
    #     print("account num: ",account.account_number)
    #     print("name: ", account.name)