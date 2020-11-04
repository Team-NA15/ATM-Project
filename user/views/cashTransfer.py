from ..decorator import user_authenticated

#GET request to load page with form for cash transfer
@user_authenticated
def cashTransfer(request): 
    #logic for loading cash transfer page
    return 