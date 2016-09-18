from django.contrib.auth.models import Group


def create(group_name):
    newgroup = Group.objects.create(name=group_name)
    newgroup.save()
    
def find(groupname):
    return Group.objects.get(name=groupname)