from zerxis_twitter.models import zerxis_user
from django.contrib import admin


##class TwitterUserOption(admin.ModelAdmin):
##    """Zerxis twitter user options"""
##    search_fields = ('username', 'oauth_key')

##admin.site.register(twitter_user,TwitterUserOption)
admin.site.register(zerxis_user)
