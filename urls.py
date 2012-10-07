from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from avatar import urls as avatar_urls

from voting.views import vote_on_object

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import login, logout

from django.views.generic import ListView, TemplateView

from strifepark.views import index


urlpatterns = patterns('',
    #url(r'^$', direct_to_template, {'template': 'index.html'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^$', 'strifepark.blog.blog'),                
    (r'^user/$', 'user_profile.views.show_perms'),
    (r'^blog/$','strifepark.blog.blog'),
    (r'^compose/$','strifepark.blog.post'),
                   
    (r'^blog/edit/(?P<entry_slug>\w+.+\w+)/$','strifepark.blog.edit'),
    (r'^blog/(?P<entry_slug>\w+.+\w)/$','strifepark.blog.entry'),
                       

    (r'^zerxis/$','zerxis.views.status_update'),
    (r'^zerxis/user/(?P<user_name>\w+)/$','zerxis.views.user_stream'),
    (r'^zerxis/search/$','zerxis.views.search'),
    (r'^zerxis/mentions/$','zerxis.views.user_mentions'),
    (r'^zerxis/directs/$','zerxis.views.user_directs'),
    (r'^search/$','strifepark.blog.search'),
    (r'^books$','strifepark.views.books'),
    (r'^index$','strifepark.views.index'),
             
    (r'^accounts/login/$','strifepark_login.views.login'),
    (r'^accounts/logout/$','strifepark_login.views.logout'),

    (r'^accounts/user/(?P<user_name>\w+)/$','user_profile.views.profile'),
    (r'^accounts/$','user_profile.views.profile'),
    (r'^accounts/',include(avatar_urls)),

    (r'^vote/(?P<model>\w+)/(?P<object_id>\w+)/(?P<direction>\w+)/$','voting.views.vote_on_object'),



)

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
