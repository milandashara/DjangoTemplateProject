from myapp.buisness import ip_range as ip_range_bll

def save(start_ip, end_ip,user):
    return ip_range_bll.save(start_ip, end_ip,user)

def get():
    return ip_range_bll.get() 

def delete(id, user):
    return ip_range_bll.delete(id,user)

def ip_range_check(ip):
    return ip_range_bll.ip_in_range(ip)