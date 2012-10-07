from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core.urlresolvers import reverse
import django.utils.encoding
from django.http import Http404
from django.template import RequestContext, Template, Context
from zerxis.forms import UpdateForm
from zerxis.actions import tweet
from zerxis import twitter
import re

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
    
    return render_to_response('bs/twitter/zerxis_tab1.html',{
        'title':'Zerxis','truncate':True,'text':user_name,'zerxis_user':user,'form':UpdateForm,'Updates':statuses},context_instance=RequestContext(request))

def user_directs(request):
    form = UpdateForm()
    api = get_api()
    statuses = api.GetDirectMessages()
    linkify_statuses(statuses)
    return render_to_response('bs/twitter/zerxis_tab1.html',{
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
    return twitter.Api(consumer_key='ih5MerLMDnRSTURoAJM4oQ',
                        consumer_secret='XJ8Y59Uy1vNS5k4GjNrbSgqZAjqyGiBvFZsHMY',
                        access_token_key='48656739-jZfVsVGHsHiqNDHN6CbzcXyoqq2UO6sXcUMVhIpI',
                        access_token_secret='JV1driFeXOAOGUjRM8rXTGPRDR5MokcMOnHe11raA')
	#add the consumer_key and access tokens
    return twitter.Api(consumer_key='',
                        consumer_secret='',
                        access_token_key='',
                        access_token_secret='')
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

def search(request):
 
    query = request.GET.get('q','')
    page = request.GET.get('page','')

    results = []
        
    p = Paginator(results,4)
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
    return render_to_response('bs/twitter/zerxis_tab1.html',{
        'title':'Search','Entry':entries.object_list,'paginator':entries,'q':query,'truncate':True},context_instance=RequestContext(request))
