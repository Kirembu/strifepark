from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User,unique=True)
    phone = models.CharField(max_length=24,blank=True)
    favourite_band = models.CharField(max_length=100, blank=True)
    phone_provider = models.CharField(max_length=50,blank=True)
    '~django.db.models.Model.__unicode__'

    def __unicode__(self):
        return self.user.username
    
