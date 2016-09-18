import re;
import subprocess
import datetime
import os
from django.http.response import HttpResponse
import mimetypes
import urllib


try:
    from ipaddress import ip_address
except ImportError:
    from ipaddr import IPAddress as ip_address
    
def validate_ip(ip):
    if re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$', ip):  
        return True
    else:
        return False


def subprocess_bg_cmd(command):
    process = subprocess.Popen(command, shell=True, bufsize=1)
    return process.pid


def subprocess_back_cmd(command):
    subprocess.Popen(command, shell=True, bufsize=1)
    return 1


def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, bufsize=1)
    proc_stdout = process.communicate()[0].strip()
    return str(proc_stdout)


def password_validator(password):
    if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,10}', password):
        return True
    else:
        return False


def get_now():
    return datetime.datetime.now()


def findIPs(start_ip, end_ip):
    start_ip = ip_address(start_ip)
    end_ip = ip_address(end_ip)
    result = []
    while start_ip <= end_ip:
        result.append(str(start_ip))
        start_ip += 1
    return result


def ip_in_range(start_ip, end_ip, ip):
    ips = findIPs(start_ip, end_ip)
    if ip in ips:
        return True
    return False


def ping(ip_address):
    response = os.system("ping -c 1 " + ip_address)
    
    # and then check the response...
    if response == 0:
        print ip_address, 'is up!'
        return True,[]
    else:
        print ip_address, 'is down!'
        return False,['cannot ping '+ip_address]


def download_file_util(request,file_path, original_filename):
    try:
        fp = open(file_path, 'rb')
        response = HttpResponse(fp.read())
        response['Content-Length'] = str(os.stat(file_path).st_size)
        fp.close()
    except OSError:
        response = HttpResponse()
    except IOError:
        response = HttpResponse()
        
    type, encoding = mimetypes.guess_type(original_filename)
    if type is None:
        type = 'application/octet-stream'
    response['Content-Type'] = type
    
    if encoding is not None:
        response['Content-Encoding'] = encoding

    # To inspect details for the below code, see http://greenbytes.de/tech/tc2231/
    if u'WebKit' in request.META['HTTP_USER_AGENT']:
        # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
        filename_header = 'filename=%s' % original_filename.encode('utf-8')
    elif u'MSIE' in request.META['HTTP_USER_AGENT']:
        # IE does not support internationalized filename at all.
        # It can only recognize internationalized URL, so we do the trick via routing rules.
        filename_header = ''
    else:
        # For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
        filename_header = 'filename*=UTF-8\'\'%s' % urllib.quote(original_filename.encode('utf-8'))
    response['Content-Disposition'] = 'attachment; ' + filename_header

        
    return response






if __name__ == '__main__':
    print validate_ip('ip')
    print validate_ip('0.0.0.0')
    print password_validator('password')
    print password_validator('Amit@2015')
    print password_validator('Am@2015')
    print get_now()
    print(findIPs('111.111.111.0', '111.111.111.3'))
    print ip_in_range('111.111.111.0', '111.111.111.3', '111.111.111.2')
    args = 'mgt 192.168.8.10/24 192.168.8.1 8.8.8.8'

    print ping('192.168.8.123')
