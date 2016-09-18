from django.contrib.auth.models import Permission
from django.contrib.auth.backends import ModelBackend


def readwrite_perm_required(view):
    def wrapper(request, *args, **kwargs):
        is_authorized = True

        if not request.user.has_perm('auth.readwrite'):
           is_authorized = False
        
        return view(request, is_authorized)
        
    return wrapper 