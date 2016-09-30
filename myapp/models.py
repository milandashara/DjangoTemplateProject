from django.db import models

from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from djmoney.models.fields import MoneyField
from django_countries.fields import CountryField

class ip_range(models.Model):
    pub_date = models.DateTimeField('date published')
    start_ip_address = models.GenericIPAddressField()
    end_ip_address = models.GenericIPAddressField()
    

class Restaurant(models.Model):
    logo = models.ImageField('Restaurant Logo')
    name = models.CharField('Restaurant Name',max_length=100)
    address = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = CountryField()
    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s" % self.name

class MenuGroup(models.Model):
    name = models.CharField(max_length=100) 
    restuarant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s" % self.name
    
class Menu(models.Model):
    item_name = models.CharField('Item Name',max_length=100)
    item_image = models.ImageField('Item Image')
    description = models.CharField(max_length=100)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='INR')
    menu_group = models.ForeignKey(MenuGroup, on_delete=models.CASCADE)
    def __str__(self):
        return self.item_name

    def __unicode__(self):
        return u"%s" % self.item_name
    

    
