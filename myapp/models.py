from django.db import models

from datetime import datetime
from django.contrib.auth.models import User
 
class ip_range(models.Model):
    pub_date = models.DateTimeField('date published')
    start_ip_address = models.GenericIPAddressField()
    end_ip_address = models.GenericIPAddressField()
    
# class activity_log(models.Model):
#     pub_date = models.DateTimeField(default = datetime.utcnow)
#     description = models.TextField()
#     status = models.TextField(default = 'success')
#     user = models.ForeignKey(User, default = None, null = True)
#     
# class configuration(models.Model):
#     created_date = models.DateTimeField(default = datetime.utcnow, null = True)
#     updated_date = models.DateTimeField(default = datetime.utcnow, null = True)
#     name = models.TextField(primary_key=True)
#     user = models.ForeignKey(User, default = None, null = True)
#     value = models.TextField(null = True)