from strifepark_login.models import spUserProfile
from django.contrib import admin


class UserProfileOption(admin.ModelAdmin):
    """User profile stuff"""
    search_fields = ('bio',)
    list_select_related = True

admin.site.register(spUserProfile,UserProfileOption)
