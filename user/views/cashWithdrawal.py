from ..decorator import user_authenticated

#GET request to load page with form for withdrawing money 
@user_authenticated
def cashWithdrawal(request): 
    #logic for loading page for money withdrawal 
    return 