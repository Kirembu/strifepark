from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core import serializers

from strifepark_login.models import *
from django.db.models import Q
'''Import forms and User profile'''
from strifepark_login import forms as myforms
from django.core.mail import *
import datetime
from time import mktime
from django.core.mail import EmailMultiAlternatives
from strifepark_login.models import PasswordChangeRequest
import threading

#Global Timer Object
Timer = None
def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
def login(request):
    if request.method == 'POST':
        redirect_to = request.GET.get('next')
	if not request.user.is_authenticated():
		forms = myforms.LoginForm(request.POST)
		if forms.is_valid():
			user = authenticate(username=forms.cleaned_data["username"],password=forms.cleaned_data["password"])
			
                        if not redirect_to:
                            redirect_to = settings.LOGIN_REDIRECT_URL

			if user is not None:
				auth_login(request,user)
				if not forms.cleaned_data["remember"]:
                                    request.session.set_expiry(3000)
				request.session['member_id'] = user.id
				return HttpResponseRedirect(redirect_to)
			else:
				return render_to_response('bs/login.html',{'form':forms,
                                                                                  'error':True,},context_instance=RequestContext(request))
		else:
			return render_to_response('bs/login.html',{'form':forms,'login':True,'data':request.POST},context_instance=RequestContext(request))
	else:
            return HttpResponseRedirect('/blog/compose/')
    else:
        forms = myforms.LoginForm()
      
    return render_to_response('bs/login.html',
                              {'title':'Login',
                               'form':forms},context_instance=RequestContext(request))
		

def logout(request):
    auth_logout(request)
    return render_to_response('bs/registration/logged_out.html',{},context_instance=RequestContext(request))
