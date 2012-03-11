from user_profile.models import UserProfile
from django.contrib import admin


class UserProfileOption(admin.ModelAdmin):
    """User profile stuff"""
    search_fields = ('phone', 'favourite_band')
    list_select_related = True

admin.site.register(UserProfile,UserProfileOption)
