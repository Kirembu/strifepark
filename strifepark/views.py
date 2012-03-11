from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core.urlresolvers import reverse
import django.utils.encoding
from django.http import Http404
from django import forms
from django.db import models
from django.template import RequestContext, Template, Context
from django.forms import ModelForm
from django.template.defaultfilters import slugify
from django.utils.decorators import method_decorator
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

import functools
import markdown
import os.path
import re
import unicodedata


from strifepark.models import Entry
from polls.models import Poll, Choice

from strifepark.pytext import pyText
import datetime
from strifepark.forms import EntryForm


def about(request):
    return render_to_response('bs/about.html',{
        'title':'About',
        'ip_address':request.META['REMOTE_ADDR']},context_instance=RequestContext(request))

def alice(request):
    content = pyText()
    t = content.createdicts('c:/kirembu/mysite/mysite/static/text/lc.txt')
    return render_to_response('bs/alice.html',{
        'text':sorted(t.keys()),
        'title':'For Alice',},context_instance = RequestContext(request))

def results(request,chapter_no='none'):

    text = pyText()
    te = text.createdicts('static/text/lc.txt')
    try:
        entry = te[chapter_no]
    except (KeyError):
        raise Http404
    else:    
        return render_to_response('bs/alice.html', {r'entry':markdown.markdown(entry),
                                                        'title':chapter_no,
                                                        'user':'coder',
                                                        'ip_address': request.META['REMOTE_ADDR']},
                                                        context_instance=RequestContext(request))

def editText(request, chapter_no='none'):
    text = pyText()
    te = text.createdicts('static/text/lc.txt')
    try:
        entry = te[chapter_no]
    except (KeyError):
        raise Http404
    else:
        
        form = EntryForm(initial = {'title':chapter_no,
                                    'slug':slugify(chapter_no),
                                    'markdown':entry})
        #form.author=instance = 'kirembu'
        #form.title={initial= 'title'='hello'}
        return render_to_response('bs/compose.html', {'form':form,
                                                            'title':chapter_no,                                                               
                                                         'ip_address': request.META['REMOTE_ADDR']}, context_instance=RequestContext(request))
def books(request):
    return render_to_response('strifepark/books.html')

def index(request):
    return render_to_response('bs/polls.html',
                              {'poll':Poll.objects.all(),
                               
                               }, context_instance=RequestContext(request))

def messages_seen(request):
    storage = get_messages(request)
    for message in storage:
        msg.append(message)
    return render_to_response('bs/messages.html', {}, context_instance=RequestContext(request))

    
def messages(request):
    msg =[]
    storage = get_messages(request)
    for message in storage:
        msg.append(message)
    storage.used = False
    return render_to_response('bs/messages.html', {'notifications':msg,'number':len(msg)}, context_instance=RequestContext(request))

def msgCount(request):
    msg =[]
    storage = get_messages(request)
    for message in storage:
        msg.append(message)
    storage.used = False
    return render_to_response('bs/msgcount.html', {'number':len(msg)}, context_instance=RequestContext(request))
