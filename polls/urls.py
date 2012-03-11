from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    (r'^polls/$', 'polls.views.index'),
    (r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    (r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    (r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    (r'^polls/latest\.php$', 'polls.views.index'),
    (r'^search/', 'polls.views.search'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    )
