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
from django.views.generic.simple import redirect_to

from zerxis.views import zerxis_home, login, done, error, form, form2, user_stream
from zerxis.facebook import facebook_view

urlpatterns = patterns('',
    #url(r'^$', direct_to_template, {'template': 'index.html'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^$', 'strifepark.views.landing'),                
    (r'^user/$', 'user_profile.views.show_perms'),
    (r'^blog/$','strifepark.blog.blog'),
    (r'^compose/$','strifepark.blog.post'),
                   
    (r'^blog/edit/(?P<entry_slug>\w+.+\w+)/$','strifepark.blog.edit'),
    (r'^blog/d/(?P<entry_slug>\w+.+\w+)/$','strifepark.blog.delete'),
    (r'^blog/(?P<entry_slug>\w+.+\w)/$','strifepark.blog.entry'),
                       

    url(r'^zerxis/user/(?P<user_name>\w+)/$', user_stream, name='user_stream'),
    url(r'^zerxis/login/$', login, name='zerxis_login'),
    (r'^zerxis/search/$','zerxis.views.search'),
    (r'^zerxis/mentions/$','zerxis.views.user_mentions'),
    (r'^zerxis/directs/$','zerxis.views.user_directs'),
    (r'^search/$','strifepark.blog.search'),
    (r'^index$','strifepark.views.index'),
             
    (r'^accounts/login/$','strifepark_login.views.login'),
    (r'^accounts/logout/$','strifepark_login.views.logout'),

    (r'^accounts/user/(?P<user_name>\w+)/$','user_profile.views.profile'),
    (r'^accounts/$','user_profile.views.profile'),
    (r'^accounts/',include(avatar_urls)),
    (r'^about/$', redirect_to, {'url': 'http://about.me/kirembu'}),

    (r'^vote/(?P<model>\w+)/(?P<object_id>\w+)/(?P<direction>\w+)/$','voting.views.vote_on_object'),

    url(r'^zerxis/$', zerxis_home, name='zerxis_home'),
    url(r'^done/$', done, name='done'),
    url(r'^error/$', error, name='error'),
    url(r'^form/$', form, name='form'),
    url(r'^form2/$', form2, name='form2'),
    url(r'^fb/', facebook_view, name='fb_app'),
    url(r'^zerxis/', include('social_auth.urls')),

    (r'^robots.txt', TemplateView.as_view(template_name="robots.txt")),
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
