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
import tornado.web
import tornado.wsgi
import unicodedata
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from strifepark.models import Entry
from strifepark.forms import EntryForm
from django.template.defaultfilters import slugify
import datetime
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def blog(request):
    entry_list = Entry.objects.all().order_by('-pub_date')
    
    p = Paginator(entry_list,4)
    if request.GET.get('page'):
        
        page = request.GET.get('page')
    else:
        page = 1
        
    try:
        entries = p.page(page)
    except PageNotAnInteger:
        entries = p.page(1)
    except EmptyPage:
        entries = p.page(p.num_pages)
    
    return render_to_response('strifepark/home.html',{
        'title':'Strife Park','Entry':entries.object_list,'paginator':entries,'truncate':True},context_instance=RequestContext(request))
def entry(request,entry_slug):
    
    an_entry = Entry.objects.filter(slug=entry_slug).get()

    if not an_entry:
        raise Http404
    return render_to_response('strifepark/entry.html',{
        'title':'Title: ' + an_entry.title,'Entry':an_entry,'truncate':False},context_instance=RequestContext(request))
def edit(request,entry_slug):

    entry_list = Entry.objects.filter(slug=entry_slug).get()
    p = entry_list
     
    form = EntryForm(initial={'markdown': p.body,
                              'title': p.title,
                              'slug':p.slug,
                              'author':p.author,
                              'pub_date':p.pub_date,
                              })
    if not entry_list:
        raise Http404
    return render_to_response('strifepark/edit.html',{
        'title':'Strife Park','form':form,'key':p.pk},context_instance=RequestContext(request))
def get(request,key=None):
    entry = Entry.objects.get(pk=key) if key else None
    return render_to_response('strifepark/results.html')

def post(request):
    
    if request.method == 'POST':
        form = EntryForm()
        if form.is_valid:
            key = request.POST['key']
            
            if not key:
                entry = Entry()
                entry_slug = slugify(request.POST['title'])
                while True:
                    existing = Entry.objects.filter(slug=entry_slug)
                    if not existing:
                        entry.slug = entry_slug
                        break
                    entry_slug += "-2"
                    
            else:            
                entry = Entry.objects.get(pk=key)        
            entry.title = request.POST['title']
            entry.body = request.POST['markdown']
            entry.markdown =markdown.markdown(request.POST['markdown'])
            entry.pub_date =request.POST['pub_date']
            entry.updated = datetime.datetime.today()
            entry.author = request.user
            entry.save()
            return HttpResponseRedirect('/post/'+entry.slug)
        else:
            form = EntryForm()
        
    else:
        form = EntryForm()
    return render_to_response('strifepark/edit.html',
                              {'title':'ADD NEW',
                               'form':form},context_instance=RequestContext(request))
