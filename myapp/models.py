from django.db import models

from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.gis.db import models

class ip_range(models.Model):
    pub_date = models.DateTimeField('date published')
    start_ip_address = models.GenericIPAddressField()
    end_ip_address = models.GenericIPAddressField()
    

class Restaurant(models.Model):
#     name = models.CharField(max_length=200)
    logo = models.ImageField('Company Logo')
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
  



# class Zipcode(models.Model):
#     code = models.CharField(max_length=5)
#     poly = models.PolygonField()
# 
# 
# 
# class Address(models.Model):
#     num = models.IntegerField()
#     street = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=2)
#     zipcode = models.ForeignKey(Zipcode, on_delete=models.CASCADE)
#     objects = models.GeoManager()
    
