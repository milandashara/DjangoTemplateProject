from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Group
from myapp.dao import user_group_dao
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from __builtin__ import str


def create_user(username, email, password,groupname):
    try:
        user = User.objects.create_user(username, email, password)
        user.groups.add(user_group_dao.find(groupname))
        user.save()
        return True,[]
    except Exception, e:
        print str(e)
        return False,['username Already Exist']
    
def change_password(username,new_password):
    u = find_by_username(username)
    u.set_password(new_password)
    u.save()

def find_by_username(username):
    return User.objects.get(username = username)
    
def get_users(page):
    user_list = User.objects.all()
    paginator = Paginator(user_list, 8) # Show 25 contacts per page
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        users = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        users = paginator.page(paginator.num_pages)

    return users

def delete_user(username):
    try:
        user = find_by_username(username)
        user.delete()
        return True,[]
    except Exception,e:
        return False,['User does not Exist']
        
    
def edit_user(username,email,password,role):
    try:
        user = find_by_username(username)
        user.set_password(password)
        user.email = email
        user.groups.clear()
        user.groups.add(user_group_dao.find(role))
        user.save()
        return True,[]
    except Exception,e:
        print str(e)
        return False,['Error while editing User'];
    



    