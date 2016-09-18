from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse


import logging
from myapp import authorization
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from myapp.service import ip_range as ip_range_service
from lockout.exceptions import LockedOut

# Get an instance of a logger
logger = logging.getLogger(__name__)

from django import forms

class LoginForm(forms.Form):
    username = forms.TextInput()
    password = forms.TextInput()

def login_locked_view(request):
    context = {}
    context['errors'] = ['Your account has been locked out because of too many failed login attempts. Please login after 10 minutes.']
    return login_view(request,context_dict=context)

def login_view(request,context_dict={}):
    context = context_dict
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            errors = []
            
            #ip range check
            client_ip = get_client_ip(request)
            is_client_allowed,errors = ip_range_service.ip_range_check(client_ip)
            username=request.POST['username']
            if not is_client_allowed:
                context['errors'] = errors
                activity_log_input = {}
                activity_log_input['status'] = 'error'
                activity_log_input['description'] = username +' tried to login. '+'Login from '+client_ip + ' is not allowed'
                
                form = LoginForm()
                context['form'] = form
                return render(request,'login/index.html', context)
            #is_success, errors = login.user_authentication( request.POST['username'], request.POST['password'] )
            try:
                user = authenticate(username=username, password=request.POST['password'])
            except LockedOut:
                activity_log_input = {}
                activity_log_input['status'] = 'error'
                activity_log_input['description'] = 'Your account has been locked out because of too many failed login attempts. Please login after 10 minutes.'
                activity_log_input['user'] = None

                form = LoginForm()
                context['form'] = form
                context['errors'] = ['Your account has been locked out because of too many failed login attempts. Please login after 10 minutes.']
                return render(request,'login/index.html', context)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    activity_log_input = {}
                    activity_log_input['description'] = user.username +' successfully logged in from '+client_ip + ' '
                    activity_log_input['user'] = user
            
                    return redirect('myapp:switch-mode')
                    # Redirect to a success page.
                else:
                # Return a 'disabled account' error message
                    context['errors'] = ['User is Disabled']
                    form = LoginForm()
                    context['form'] = form
                    return render(request,'login/index.html', context)
            else:
                context['errors'] = ['Invalid Credential']
                activity_log_input = {}
                activity_log_input['status'] = 'error'
                activity_log_input['description'] = username +' enter invalid credential to login from '+client_ip + ' '
                activity_log_input['user'] = None
             
                form = LoginForm()
                context['form'] = form
                return render(request,'login/index.html', context)
            
    else:
        if request.user.is_authenticated():
            return redirect('myapp:switch-mode')
        else:
            form = LoginForm()
            context['form'] = form
            return render(request, 'login/index.html', context)

@login_required(login_url='myapp:login')
def logout_view(request):
    activity_log_input = {}
    activity_log_input['description'] = request.user.username +' logout successully'
    activity_log_input['user'] = request.user

    logout(request)
    
    return redirect('myapp:login')
    # Redirect to a success page.


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
