from django.db import models
from django.contrib.auth.models import User

class spUserProfile(models.Model):
    user = models.ForeignKey(User)
    bio = models.CharField(max_length=160,null=True,blank=True)
    url = models.URLField(null=True,blank=True)
    phone = models.CharField(max_length=25,null=True,blank=True)
    
class LoginStatus(models.Model):
    userid = models.ForeignKey(User)
    status = models.BooleanField()
    
class PasswordChangeRequest(models.Model):
    account = models.ForeignKey(User)
    req_random_key = models.CharField(max_length = 48)
    created_at = models.DateTimeField()
    
