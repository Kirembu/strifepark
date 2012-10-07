from django.db import models
from django.contrib.auth.models import User
from zerxis.models import zerxis_user
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User,unique=True)
    phone = models.CharField(max_length=24,blank=True)
    favourite_band = models.CharField(max_length=100, blank=True)
    phone_provider = models.CharField(max_length=50,blank=True)
##    facebook = models.CharField(max_length=50,blank=True)
##    twittter = models.CharField(max_length=50,blank=True)
##    rss = models.CharField(max_length=50,blank=True)
##    bio = models.CharField(max_length=160,blank=True,null=True)
##    url = models.URLField(blank=True,null=True)
    #username = models.ForeignKey(zerxis_user,blank=True,null=True)
    '~django.db.models.Model.__unicode__'

    def __unicode__(self):
        return self.user.username
    
