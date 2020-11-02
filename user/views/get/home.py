from django.shortcuts import render 
from user.models import AccountExtension

#GET request loads page with options for ATM cardholder 
def home(request): 
    #HARDCODED EXAMPLE OF MODEL CREATION
    # acc = AccountExtension(
    #     account_number = 2222222233,
    #     name = 'john doe', 
    #     phone_number = '569-1624', 
    #     balance = 10000000
    # )  
    # accounts = AccountExtension.objects.all()
    # for account in accounts: 
    #     print("account num: ",account.account_number)
    #     print("name: ", account.name)
    return render(request, 'user/home.html')