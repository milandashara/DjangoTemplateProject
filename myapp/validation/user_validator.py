'''
Created on 9 May 2016

@author: milanashara
'''
from myapp.utility import common_utility

def validate_user(username, email, password, groupname):
    if not username or not email or not password or not groupname:
        return ['All Fields are mandatory']
    
    if not common_utility.password_validator(password):
        return ['Password must be minimum 8 characters in length with atleast 1 uppercase, 1 lowercase, 1 number and 1 special character']

