# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound

def show_color(request):
    if request.method == 'GET':
        if "favorite_color" in request.GET:
            response = HttpResponse("Your favorite color is now %s" % \
                                    request.GET["favorite_color"])
            response.set_cookie("favorite_color",request.GET["favorite_color"])
            return response
        else:

            if "favorite_color" in request.COOKIES:
                
                return HttpResponse("Your favorite color is %s" %\
                                    request.COOKIES["favorite_color"])
            else:
                return HttpResponse("You don't have a favorite color.")
