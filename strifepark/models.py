from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Entry(models.Model):
    """A single blog entry."""
    '~django.db.models.Model.__unicode__'

    def __unicode__(self):
        return self.title
    
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    markdown = models.TextField()
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    updated = models.DateTimeField('date updated')
    class Admin:
        search_fields = ('title',)
    class Meta:
        ordering =["-pub_date"]
