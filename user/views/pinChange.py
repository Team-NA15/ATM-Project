from ..decorator import user_authenticated

#Request for loading pin change form 
@user_authenticated
def pinChange(request): 
    #logic for loading page goes here 
    return