from django.db import models
class zerxis_user(models.Model):

    username = models.CharField(max_length=64,unique=True)
    oauth_key = models.CharField(max_length=128)
    oauth_secret = models.CharField(max_length=128)

    'django.db.models.Model.__unicode__'
    def __unicode__(self):
        return self.username
