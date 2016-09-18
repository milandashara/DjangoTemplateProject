

from django.shortcuts import render, redirect

from myapp.service import user_service, ip_range as ip_range_service
from django.contrib.auth.decorators import login_required
from myapp.authorization.permission import readwrite_perm_required
from myapp import constants
import logging

logger = logging.getLogger(__name__)
feature_title = 'IP Range Setting'

@login_required(login_url='myapp:login')
@readwrite_perm_required
def get_ip_range_setting_view(request,context = {}, is_authorized = True):
    
    try:
        context['title'] = feature_title
    except Exception,e:
        context = {}
        context['title'] = feature_title
    context['menu_ip_range_active'] = True
    context['menu6'] = "true"
    if not is_authorized:
        context['errors'] = [constants.notauth_msg]   
        return render(request, 'not_authorized.html', context)
    if request.method == 'POST':
        if not is_authorized:
            context['errors'] = [constants.notauth_msg]
        else:
            start_ip = request.POST['start_ip']
            end_ip = request.POST['end_ip']
            logger.info('get_ip_range_setting_view start ip:'+ start_ip +' end_ip:'+end_ip)
            if start_ip:
                start_ip = start_ip.strip()
            if end_ip:
                start_ip = end_ip.strip()
            is_success, errors = ip_range_service.save(start_ip, end_ip, request.user)
            if is_success:
                context['success_msg'] = 'IP Setting Saved Successfully'
            else:
                context['errors'] = errors
    
    #get existing ip
    ip_range_model,is_success,errors = ip_range_service.get()
    if is_success and ip_range_model:
        context['ip_range_model'] = ip_range_model
    else:
        context['errors'] = errors
    
    
    return render(request, 'ip_range_setting/index.html', context)

@login_required(login_url='myapp:login')
@readwrite_perm_required
def delete_ip_range_view(request, is_authorized = True):
    context = {}
    context['title'] = feature_title
    context['menu_ip_range_active'] = True
    context['menu6'] = "true"
    if not is_authorized:
        context['errors'] = [constants.notauth_msg]   
        return render(request, 'not_authorized.html', context)
    else:
        ip_range_id = request.GET.get('id')
        logger.info('delete_ip_range_view  ID:'+ ip_range_id)
        is_success, errors = ip_range_service.delete(ip_range_id,request.user)
        if is_success:
            context['success_msg'] = 'IP Setting Deleted Successfully'
        else:
            context['errors'] = errors
    
    return get_ip_range_setting_view(request,context,is_authorized)
        
                