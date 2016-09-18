from myapp.utility import common_utility
from myapp.dao import ip_range_dao


def save(start_ip, end_ip,user):
    errors = []
    
    if not (common_utility.validate_ip(start_ip) or common_utility.validate_ip(end_ip)):
        return False,['Invalid IP Address']
    is_success,errors = ip_range_dao.save(start_ip.strip(),end_ip.strip())
    
        
    return is_success,errors;

def get():
    return ip_range_dao.get_ip_range()

def delete(id, user):
    if not id:
        return False,['Invalid id']
    is_success,errors = ip_range_dao.delete(id)
    
    return is_success,errors;

def ip_in_range(ip_address):
    if not (common_utility.validate_ip(ip_address)):
        return False,['Invalid IP Address']
    
    ip_range_model, is_success, errors = get()
    if not is_success:
        return False,errors
    else:
        
        #no ip range setting saved
        if not ip_range_model:
            return True,[]
        else:
            is_in_range = common_utility.ip_in_range(ip_range_model.start_ip_address, ip_range_model.end_ip_address, ip_address)
            if is_in_range:
                return True,[]
            else:
                return False,['You are not authorized to access through this client']