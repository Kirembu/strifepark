# -*- coding: utf-8 -*-

from django.conf import settings

# LiveJournal username
LJ_USERNAME     = getattr(settings, 'LJ_USERNAME', '')

# LiveJournal password's MD5 hash
LJ_PASSWORD_MD5 = getattr(settings, 'LJ_PASSWORD_MD5', '')

# A local blog entry model in the form 'app_name.model_name'.
# Example: 'myblog.Post'
BLOG_ENTRY_MODEL = getattr(settings, 'LJ_BLOG_ENTRY_MODEL', '')

# It is good practice to add the blog entry model a boolean field that would allow crossposting.
# If it is not specified at all, crossposting is done unconditionally.
BLOG_ENTRY_CROSSPOST_FIELD = getattr(settings, 'LJ_BLOG_ENTRY_CROSSPOST_FIELD', '')
