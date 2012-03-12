
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound,Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from strifepark.models import Entry
from django.contrib.auth.models import User

def show_color(request,user_name=None):
    if "favorite_color" in request.COOKIES:
        return HttpResponse(user_name+" Your favorite color is %s" %\
                            request.COOKIEW["favorite_color"])
    else:
        if request.user.username == user_name:
            s = "You don't"
        else:
            s = 'Does not'
        
        
        return HttpResponse("%s  have a favorite color." %s
)

def set_color(request):
    if "favorite_color" in request.GET:
        response = HttpResponse("Your favorite color is now %s" % \
                                request.GET["favorite_color"])
        response.set_cookie("favorite_color",request.GET["favorite_color"])
        return response
    else:
        return HtttpResponse ("You didn't give a favorite color.")

    
def show_perms(request):
    return render_to_response('bs/user/user_profile.html',{
        'title':'User',},context_instance=RequestContext(request))

def profile(request,user_name=None):
    if not user_name:
        user_name = request.user.username
    update_count = Entry.objects.filter(author = user_name).count()
    try:
        last_update = Entry.objects.filter(author = str(user_name)).latest('pub_date')
    except:
        last_update = None
    try:
        p = User.objects.get(username=user_name).get_profile()
    except:
        raise Http404
        
    return render_to_response('bs/user/user_profile.html',{
        'title':'Profile',
        'profile':p,
        'update_count':update_count,
        'last_update':last_update},context_instance=RequestContext(request))
