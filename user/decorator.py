from django.shortcuts import redirect

def user_authenticated(function): 
    def wrap(request, *args, **kwargs): 
        if 'token' not in request.session: 
            return redirect('/user/cardholder-login')
        else: 
            print('user logged in')
            return None
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
