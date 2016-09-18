from myapp.models import ip_range
import datetime
from __builtin__ import str
import logging

#logger = logging.getLogger(__name__)
def save(start_ip, end_ip):
    try:
        #remove prev
        ip_range.objects.all().delete()
        
        #save new
        ip_range_model = ip_range()
        ip_range_model.start_ip_address = start_ip
        ip_range_model.end_ip_address = end_ip
        ip_range_model.pub_date = datetime.datetime.utcnow()
        ip_range_model.save()
        return True,[]
    
    except Exception, e:
        #logger.error(str(e))
        return False,['Error while saving IP Range']
    
def get_ip_range():
    try:
        qs = ip_range.objects.all()
        r = list(qs[:1])
        if r:
            return r[0],True,[]
        return None,True,[]
    except Exception, e:
        #logger.error(str(e))
        return None,False,['Error while getting IP Range']
    
def delete(id):
    try:
        ip_range_model = ip_range.objects.all().get(id=id)
        ip_range_model.delete()
        return True,[]
    except Exception,e:
        return False,['Error while delete IP Range Setting']
    


