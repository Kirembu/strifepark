# -*- coding: utf-8 -*-
#
#  Copyright (c) 2009 Andy Mikhailenko and contributors
#
#  This file is part of Django LJSync.
#
#  Django LJSync is free software under terms of the GNU Lesser
#  General Public License version 3 (LGPLv3) as published by the Free
#  Software Foundation. See the file README for copying conditions.
#

" Imports LiveJournal entries to local Django database. "

# python
import sys
import time
import urllib
from datetime import date, datetime, timedelta
from optparse import make_option

# django
from django.core.management.base import BaseCommand, CommandError

# apps
from ljsync.conf.settings import LJ_USERNAME, LJ_PASSWORD_MD5
from ljsync.protocol import LiveJournalClient
from ljsync.models import LJPost

def datetime_iterator(from_date, to_date):
    while from_date <= to_date:
        yield from_date
        from_date = from_date + timedelta(days = 1)
    return

class Command(BaseCommand):
    help = """Imports LiveJournal entries to Django blog application.

           Please specify at least the date of the earliest post to be imported.
           Dates should be in the format YYYY-MM-DD, YYYY-MM or YYYY."""
    args = "from_date [to_date]"

    def handle(self, from_date, to_date=datetime.now().date(), **options):
        if not LJ_USERNAME or not LJ_PASSWORD_MD5:
            raise Exception('Please specify your LiveJournal username and '
                            'password in the site settings (see blog app settings).')

        from_date = date(*(int(x) for x in from_date.split('-')))
        if not isinstance(to_date, date):
            to_date = date(*(int(x) for x in to_date.split('-')))

        dates = datetime_iterator(from_date, to_date)

        LiveJournalImporter(LJ_USERNAME, LJ_PASSWORD_MD5).import_posts(dates)

class LiveJournalImporter(object):
    " A tool to import data from LiveJournal to the blog app. "

    def __init__(self, username, password_md5):
        if not username or not password_md5:
            raise Exception, 'Please specify your LiveJournal username and password.'
        self.lj = LiveJournalClient(username, password_md5)

    def import_posts_for_day(self, year, month, day):
        """
        Fetches posts from LiveJournal for given day and converts them into local
        LiveJournalPost objects.
        """
        info = self.lj.get_events(selecttype='day', year=year, month=month, day=day)
        events = info["events"]
        posts_cnt = 0
        for event in events:
            p = LJPost()
            for name in p._meta.get_all_field_names():
                if event.has_key(name):
                    value = event[name]
                    # decode post body
                    if name == 'event':
                        value = urllib.unquote_plus(value)
                    setattr(p, name, value)
            p.save()
            if hasattr(p, 'id') and p.id > 0:
                posts_cnt += 1
        if posts_cnt:
            sys.stdout.write('    %d posts at %s-%s-%s\n' % (posts_cnt, year, month, day))
        return posts_cnt

    def import_posts(self, dates):
        " Imports all posts for given years, months and days. "
        imported_posts_cnt = 0
        for date in dates:
            posts_cnt = self.import_posts_for_day(date.year, date.month, date.day)
            imported_posts_cnt += posts_cnt
            # ensure we don't violate the rules for bots: http://www.livejournal.com/bots/
            time.sleep(0.3)
        sys.stdout.write('Done. Imported %d posts.\n' % imported_posts_cnt)
