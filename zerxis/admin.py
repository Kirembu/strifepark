from zerxis.models import zerxis_user
from django.contrib import admin
from zerxis.models import CustomUser
#from zerxis.models import RequestLog 

class CustomUserOption(admin.ModelAdmin):
    """Custom user options"""
    search_fields = ('username', 'last_login')

admin.site.register(zerxis_user)