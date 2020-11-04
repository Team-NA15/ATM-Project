from ..decorator import user_authenticated

#GET request for loading page to check balance of account
@user_authenticated
def balanceInquiry(request): 
    #logic for loading page goes here 
    return 