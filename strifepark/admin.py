from strifepark.models import Entry
from django.contrib import admin


class EntryOption(admin.ModelAdmin):
    """Social Auth user options"""
    search_fields = ('body', 'title','author','tags')
    list_select_related = True

admin.site.register(Entry,EntryOption)
