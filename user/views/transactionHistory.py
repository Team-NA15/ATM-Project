from ..decorator import user_authenticated

#Request for viewing transaction history 
@user_authenticated
def transactionHistory(request): 
    #logic for getting transaction history goes here
    return 