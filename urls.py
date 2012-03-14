#the usual suspects in django deployment

from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


# Uncomment the next two lines to enable the admin: (done)
from django.contrib import admin
admin.autodiscover()

# The login and logout permission required fiasco I'm working on it kind of thing
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import login, logout

from django.views.generic import ListView, TemplateView

from strifepark.views import index
from strifepark.models import Entry

from social_auth import urls as social_urls
from avatar import urls as avatar_urls
from microblogging import urls as microblogging_urls

from voting.views import vote_on_object


entry_dict = {
    'model': Entry,
    'template_object_name': 'index',
    'allow_xmlhttprequest': True,
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'strifepark.blog.blog'),
    (r'^p/$','strifepark.blog.blogp'),

    (r'^messages/$','strifepark.views.messages'),
    (r'^messages/count/$','strifepark.views.msgCount'),
    (r'^messages/seen/$','strifepark.views.messages_seen'),                  
    (r'^user/$', 'user_profile.views.show_perms'),
    (r'^results/(?P<poll_id>\d+)/$', 'polls.views.results'),
    (r'^music/', 'musiclib.views.index'),
    (r'^music/search/','musiclib.views.search'),
    (r'^tester','polls.views.tester'),
    (r'^about',login_required(TemplateView.as_view(template_name='bs/login.html'))),
##    (r'^alice/$','strifepark.views.alice'),
##    (r'^alice/chapter/$','strifepark.views.results'),
##    (r'^alice/chapter/(?P<chapter_no>\w+.+\w)/edit/$', 'strifepark.views.editText'),
##    (r'^alice/chapter/(?P<chapter_no>\w.+\w)/$', 'strifepark.views.results'),

    (r'^blog/$','strifepark.blog.blog'),
    (r'^compose/$','strifepark.blog.post'),
                   
    (r'^blog/edit/(?P<entry_slug>\w+.+\w+)/$','strifepark.blog.edit'),
    (r'^blog/(?P<entry_slug>\w+.+\w)/$','strifepark.blog.entry'),
    (r'^archive/$',ListView.as_view(model = Entry)),
                       
    (r'^polls/$', 'polls.views.index'),
    (r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    (r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    (r'^polls/(?P<poll_id>\d+)/vote/$','polls.views.vote'),
    (r'^polls/latest\.php$', 'polls.views.index'),
    #(r'^polls/(?P<poll_id>\d+)/vote/up/$','polls.views.vote_up'),
    #(r'^polls/(?P<poll_id>\d+)/vote/down/$','polls.views.vote_down'),

    
    (r'^zerxis/$','zerxis_twitter.views.status_update'),
    (r'^zerxis/user/(?P<user_name>\w+)/$','zerxis_twitter.views.user_stream'),
    (r'^zerxis/search/$','zerxis_twitter.views.search'),
    (r'^zerxis/mentions/$','zerxis_twitter.views.user_mentions'),
    (r'^zerxis/directs/$','zerxis_twitter.views.user_directs'),
    (r'^search/$','strifepark.blog.search'),
    (r'^books$','strifepark.views.books'),
    (r'^index$','strifepark.views.index'),

    (r'^cookies/$','test_app.views.show_color'),                  
    (r'^accounts/login/$','strifepark_login.views.login'),
    (r'^accounts/logout/$','strifepark_login.views.logout'),

    (r'^accounts/user/(?P<user_name>\w+)/$','user_profile.views.profile'),
    (r'^accounts/$','user_profile.views.profile'),
    (r'^social/',include(social_urls)),
    (r'^accounts/',include(avatar_urls)),
    (r'^m/',include(microblogging_urls)),

    (r'^vote/(?P<model>\w+)/(?P<object_id>\w+)/(?P<direction>\w+)/$','voting.views.vote_on_object'),
    (r'^vote/(?P<object_id>\d+)/(?P<direction>up|down|clear)/?$', vote_on_object, entry_dict),


    (r'^testapp/','test_app.views.show_color'),

##    (r'^microblogging/',include(microblogging_urls)),
    
    )

# Avatar

##urlpatterns += patterns('avatar.views',
##    url('^avatar/change/$', 'change', name='avatar_change'),
##    url('^avatar/delete/$', 'delete', name='avatar_delete'),
##)

##urlpatterns += patterns

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve'),

    )
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
