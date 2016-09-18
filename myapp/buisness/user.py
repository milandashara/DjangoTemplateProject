
from myapp.validation import user_validator

from myapp.utility import common_utility
from myapp.dao import user_dao


def get_users(page):
    return user_dao.get_users(page)


def create_user(request_user_model,username,email,password,groupname):
    errors = user_validator.validate_user(username, email, password, groupname)
    if errors:
        return False,errors


    is_success, errors = user_dao.create_user(username, email, password, groupname)

    #save to activity log
    if is_success:

        if is_success:
            return True,[]
        else:
            return False,errors
    else:
        return is_success,errors


def edit_user(request_user_model, username,email, password,role):
    errors = user_validator.validate_user(username, email, password, role)
    if errors:
        return False,errors

    is_success, errors = False, []
    user = find_by_username(username)
    is_success, errors = user_dao.edit_user(username, email, password, role)

   
    return is_success,errors


def find_by_username(username):
    return user_dao.find_by_username(username)


def delete_user(request_user_model, username):
    user = find_by_username(username)
    is_success, errors = False, []

    #save to activity log
    if is_success:

        if is_success:
            return True,[]
        else:
            return False,errors
    else:
        return is_success,errors

   