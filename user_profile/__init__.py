import os.path

from django.conf import settings

TWITTER_CONSUMER_KEY = getattr(settings, 'TWITTER_CONSUMER_KEY', 'supersecretecustomerkey')
TWITTER_CONSUMER_SECRET = getattr(settings, 'TWITTER_CONSUMER_SECRET', 'supersecretecustomer')

from django.db.models import signals
from django.contrib.auth.models import User
from user_profile.models import UserProfile
