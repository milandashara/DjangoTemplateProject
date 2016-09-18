from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myapp.service import dashboard_service
from myapp.middleware import load_config_data
from myapp.authorization.permission import readwrite_perm_required
from myapp import constants

@login_required(login_url='myapp:login')
def get_switch_mode_view(request):
    context={}
    context['title'] = 'Dashboard'
    return render(request, 'dashboard/index.html', context)

