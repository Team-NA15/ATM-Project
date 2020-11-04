from django.shortcuts import redirect


def cardholderLogout(request): 
    try: 
        del request.session['token']
        return redirect('/user/cardholder-login')
    except KeyError: 
        pass 
