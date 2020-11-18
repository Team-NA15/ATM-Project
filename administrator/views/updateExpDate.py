from ..decorator import admin_authenticated

#Request to update expiration date of ATM card 
@admin_authenticated
def updateExpDate(request): 
    #logic for updating ATM card expiration date goes here 
    return