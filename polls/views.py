from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
import django.contrib.staticfiles
from django.conf import settings
from polls.models import Choice, Poll
import django.contrib.staticfiles
import datetime
# ...
def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
			selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
                # Redisplay the poll voting form.
			return render_to_response('wing-the-air/polls/detail.html', {
				'poll': p,
				'error_message': "You didn't select a choice.",
				}, context_instance=RequestContext(request))
        else:
			selected_choice.votes += 1
			selected_choice.save()
			# Always return an HttpResponseRedirect after successfully dealing
			# with POST data. This prevents data from being posted twice if a
			# user hits the Back button.
			return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
def results(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('wing-the-air/polls/results.html', {'poll': p})


def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')
	return render_to_response('wing-the-air/polls/home.html', {'title':'Polls',
                                                      'polls_list':latest_poll_list,}, context_instance=RequestContext(request))
def user(request):
	latest_choice = Poll.objects.all().order_by('-pub_date')[:5]
	output =latest_choice
	return HttpResponse(output)
	
def detail(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('wing-the-air/polls/detail.html', {'poll': p,
                                                         'title':'Poll Results',
                                                         'date':datetime.date.today(),
                                                        'ip_address': request.META['REMOTE_ADDR']
                                                        },
	context_instance=RequestContext(request))
	return HttpResponse(p)
def results(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('wing-the-air/polls/results.html', {'poll': p,
                                                         'title':'Poll Results',
                                                         'date':datetime.date.today(),
                                                         'ip_address': request.META['REMOTE_ADDR']})

def login(request):
        today = datetime.date.today()
        return render_to_response('wing-the-air/polls/home.html',{'title':'Login',
                                                     'date':today,
                                                     'ip_address':request.META['REMOTE_ADDR'],})
def get_date():
        return datetime.date.today()
def tester(request):
        return HttpResponse('{{STATIC_URL}}')
