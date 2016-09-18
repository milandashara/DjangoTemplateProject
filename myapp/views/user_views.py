

from django.shortcuts import render,redirect

from myapp.service import user_service
from django.contrib.auth.decorators import login_required
from myapp.authorization.permission import readwrite_perm_required
from myapp import constants

@login_required(login_url='myapp:login')
@readwrite_perm_required
def get_user_view(request,context={},show_success = False, is_authorized = True):
    context={}
    context['title'] = 'Users'
    context['menu6'] = "true"
    context['user_menu_active'] = True
    if not is_authorized:
        context['errors'] = [constants.notauth_msg]   
        return render(request, 'not_authorized.html', context)
    if show_success:
        context['success_msg'] = 'User Saved Successfully'
    page = request.GET.get('page')
    users = user_service.get_users(page)
    context['users']=users
    return render(request, 'user/index.html', context)

@login_required(login_url='myapp:login')  
@readwrite_perm_required
def get_new_user_view(request,is_authorized = True):
    context={}
    context['title'] = 'Create New User'
    context['user_menu_active'] = True
    context['menu6'] = "true"
    if not is_authorized:
        context['errors'] = [constants.notauth_msg]   
        return render(request, 'not_authorized.html', context)
    if request.method == 'GET':
        return render(request, 'user/new.html', context)
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        groupname = request.POST['role']
        is_success,errors = user_service.create_user(request.user,username, email, password, groupname)
        if not is_success:
            context['errors'] = errors
            if not errors:
                context['errors'] = ['username Already Exists']
            
            return render(request, 'user/new.html', context)
        else:
            #context['success_msg'] = 'User Saved Successfully'
            #return render(request, 'user/new.html', context)
            #return get_user_view(request,{},True)
            return redirect('myapp:user')
            
@login_required(login_url='myapp:login')  
@readwrite_perm_required
def get_edit_user_view(request, is_authorized = True):
    context={}
    context['title'] = 'Edit User'
    context['menu6'] = "true"
    context['user_menu_active'] = True
    if not is_authorized:
        context['errors'] = [constants.notauth_msg]   
        return render(request, 'not_authorized.html', context)
    if request.method == 'GET':
        username = request.GET.get('username')
        user = user_service.find_by_username(username)
        user_form = {}
        user_form['email'] = user.email
        user_form['username'] = user.username
        for group in user.groups.all():
            user_form['role'] = group.name
        context['user_edit'] = user_form
        return render(request, 'user/edit.html', context)
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        groupname = request.POST['role']
        is_success,errors = user_service.edit_user(request.user, username, email, password, groupname)
        user_form = {}
        user_form['email'] = email
        user_form['username'] = username
        user_form['role'] = groupname
        context['user'] = user_form
        if not is_success:
            context['errors'] = errors
            if not errors:
                context['errors'] = ['Error while editing user']
            return render(request, 'user/edit.html', context)
        else:
            context['success_msg'] = 'User Updated Successfully'
            return render(request, 'user/edit.html', context)

@login_required(login_url='myapp:login')  
@readwrite_perm_required        
def get_delete_user_view(request, is_authorized = True):
    context={}
    context['title'] = 'Users'
    context['menu6'] = "true"
    context['user_menu_active'] = True
    if not is_authorized:
        context['errors'] = [constants.notauth_msg]   
        return render(request, 'not_authorized.html', context)
    if request.method == 'GET':
        username = request.GET.get('username')
        is_success = user_service.delete_user(request.user, username)
        if not is_success:
            context['errors'] = ['Error while deleting user or User does not Exist']
            return get_user_view(request)
        else:
            context['success_msg'] = username +' Deleted Successfully'
            #return get_user_view(request,context)
            return redirect('myapp:user')