from ..decorator import user_authenticated

#Request to load form for phone number change 
@user_authenticated
def phoneNumberChange(request): 
    #logic for loading page goes here  
    return