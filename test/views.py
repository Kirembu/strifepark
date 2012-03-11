#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import functools
import markdown
import os.path
import re
##import tornado.web
##import tornado.wsgi
import unicodedata
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core.urlresolvers import reverse
import django.utils.encoding
from django.http import Http404
from google.appengine.ext.db import djangoforms


from django.template import RequestContext, Template, Context
##from strifepark.models import Entry
##from strifepark.pytext import pyText

def blog(request):
    return render_to_response('home.html',{
        'title':'Strife Park',
        'ip_address': request.META['REMOTE_ADDR']},context_instance=RequestContext(request))
def about(request):
    return render_to_response('about.html',{
        'title':'About',
        'ip_address':request.META['REMOTE_ADDR']},context_instance=RequestContext(request))
def alice(request):
    content = pyText()
    t = content.createdicts('static/text/lc.txt')
    return render_to_response('strifepark/alice.html',{
        'text':sorted(t.keys()),
        'title':'For Alice',
        'ip_address': request.META['REMOTE_ADDR']},context_instance = RequestContext(request))

def results(request,chapter_no='none'):

    text = pyText()
    te = text.createdicts('static/text/lc.txt')
    try:
        entry = te[chapter_no]
    except (KeyError):
        raise Http404
    else:    
        return render_to_response('strifepark/results.html', {r'text':markdown.markdown(entry),
                                                         'title':chapter_no,
                                                        'user':'coder',
                                                         'ip_address': request.META['REMOTE_ADDR']})
def editText(request, chapter_no='none'):
    text = pyText()
    te = text.createdicts('static/text/lc.txt')
    try:
        entry = te[chapter_no]
    except (KeyError):
        raise Http404
    else:    
        return render_to_response('strifepark/edit.html', {'text':entry,
                                                         'title':chapter_no,
                                                         'ip_address': request.META['REMOTE_ADDR']}, context_instance=RequestContext(request))
def books(request):
    return render_to_response('strifepark/books.html')

class ShoutForm(djangoforms.ModelForm):
    class Meta:
        model = models.Entry
        exclude = ['pub_date','user']
    query = models.Shout.gql("ORDER BY pub_date DESC")

def index(request):
    return render_to_response('strifepark/index.html',
                              {'shouts':query.run(),
                               'from':ShoutForm()})
    
def post(request):
    from = ShoutForm(request.POST)
    if not form.is_valid():
        return render_to_response('strifepark/index.html',
                                  {'form':form})
    entry = form.save(commit=False)
    entry.user = user.get_current_user()
    entry.put()
    return HttpResponseRedirect('/')
