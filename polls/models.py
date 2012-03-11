from django.db import models

import datetime

# Create your models here.

class Poll(models.Model):
	'~django.db.models.Model.__unicode__'
	def __unicode__(self):
		return self.question
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()


class Choice(models.Model):
	'~django.db.models.Model.__unicode__'
	def __unicode__(self):
		return self.choice
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()


