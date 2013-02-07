from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import django.utils.encoding
from django.http import Http404
from django.template import RequestContext, Template, Context
from zerxis.forms import UpdateForm
from zerxis.actions import tweet
from zerxis import twitter
import re

from social_auth import __version__ as version
from social_auth.utils import setting
from social_auth.models import UserSocialAuth

import pylast

def zerxis_home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        u = request.user
        ca = UserSocialAuth.objects.all().filter(user = u).filter( provider = "twitter")
        if len(ca):
            return HttpResponseRedirect(ca[0])
        else:
            return HttpResponseRedirect('login') 
    else:
        return HttpResponseRedirect('login')

@login_required
def done(request):
    """Login complete view, displays user data"""
    ctx = {
        'version': version,
        'last_login': request.session.get('social_auth_last_login_backend')
    }
    return render_to_response('bs/zerxis/home.html', ctx, RequestContext(request))


def error(request):
    """Error view"""
    return render_to_response('bs/zerxis/error.html', {'version': version},
                              RequestContext(request))


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')

def login(request):
    """Login a user through a social account"""
    return render_to_response('bs/zerxis/login.html',{'version': version},
                         RequestContext(request))     
def search(request):
    pass
def form(request):
    if request.method == 'POST' and request.POST.get('username'):
        name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
        request.session['saved_username'] = request.POST['username']
        try:
            backend = request.session[name]['backend']
        except Exception, e:
            return redirect('%e')
        return redirect('socialauth_complete', backend=backend)
    return render_to_response('bs/zerxis/form.html', {}, RequestContext(request))

def form2(request):
    if request.method == 'POST' and request.POST.get('first_name'):
        request.session['saved_first_name'] = request.POST['first_name']
        name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
        backend = request.session[name]['backend']
        return redirect('socialauth_complete', backend=backend)
    return render_to_response('bs/zerxis/form2.html', {}, RequestContext(request))


def linkify_statuses(statuses):
    for status in statuses:
        tweet = status.text
        tweet = re.sub(r'(\A|\s)@(\w+)', r'\1<a href="/zerxis/user/\2">@\2</a>', tweet)
        status.text = re.sub(r'(\A|\s)#(\w+)', r'\1<a href="/zerxis/search?q=%23\2">#\2</a>', tweet)
    return statuses


def user_stream(request,user_name='CodeLabz'):
    api = get_api()
    user = api.GetUser(user_name)
    statuses = api.GetUserTimeline(user_name,count=5)
    linkify_statuses(statuses)
    
    return render_to_response('bs/zerxis/zerxis_userstream.html',{
        'title':'Zerxis','truncate':True,'text':user_name,'zerxis_user':user,'form':UpdateForm,'Updates':statuses},context_instance=RequestContext(request))

def user_directs(request):
    form = UpdateForm()
    api = get_api()
    statuses = api.GetDirectMessages()
    linkify_statuses(statuses)
    return render_to_response('bs/twitter/zerxis_userstream.html',{
    'title':'Zerxis - Directs',
    'Statuses':statuses,
    'form':form,},context_instance=RequestContext(request))
    
def user_mentions(request):
    form = UpdateForm()
    api = get_api()

    statuses = api.GetMentions()
    linkify_statuses(statuses)
    return render_to_response('bs/twitter/zerxis_base.html',{
    'title':'Zerxis - Mentions','Statuses':statuses,'form':form,},context_instance=RequestContext(request))
def get_api():
    return twitter.Api(consumer_key='CONSUMER_KEY',
                        consumer_secret='CONSUMER_SECRET',
                        access_token_key='ACCESS_TOKEN',
                        access_token_secret='ACCESS_TOKEN_SECRET')

def status_update(request):
    error = None
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            in_reply_to = request.POST['in_reply_to_id']
            status = request.POST['status']

            #tweet
            try:
                tweet.update_status(status)
            except:
                error = "Something went wrong with twitter :("
                    
            return HttpResponseRedirect('/zerxis/')

    else:
        api = get_api()
        try:
            
            statuses = api.GetFriendsTimeline(count=5)
            linkify_statuses(statuses)
        except:
            error = 'There was an error'
            statuses = {}
        form = UpdateForm()

    return render_to_response('bs/twitter/zerxis_tab1.html',{
    'title':'Zerxis',
    'Updates':statuses,
    'form':form,
    'error':error},context_instance=RequestContext(request))