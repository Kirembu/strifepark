from django.db import models
class zerxis_user(models.Model):

    uid = models.CharField(max_length=64,unique=True)
    access_token_key = models.CharField(max_length=128)
    access_token_secret = models.CharField(max_length=128)

    'django.db.models.Model.__unicode__'
    def __unicode__(self):
        return self.uid
