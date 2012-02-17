import urllib

from django import template
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.utils.hashcompat import md5_constructor
from user_profile.models import UserProfile

from avatar import AVATAR_DEFAULT_URL, AVATAR_GRAVATAR_BACKUP, AVATAR_GRAVATAR_DEFAULT
from user_profile import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET
register = template.Library()

def user_band(user):
    if not isinstance(user, User):
        try:
##            user = User.objects.filter(username=user).get
            band = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            return 'NONE!'
    band = band.favourite_band
    return band
register.simple_tag(user_band)
def user_fullname(user):
    if not isinstance(user, User):
        try:
            fullname = User.objects.get(user=user)
        except User.DoesNotExist:
            return 'Unnamed'
    name = fullname.full_name
    return name
register.simple_tag(user_fullname)
