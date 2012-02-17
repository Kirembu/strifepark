from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('avatar.views',
    url('^avatar/change/$', 'change', name='avatar_change'),
    url('^avatar/delete/$', 'delete', name='avatar_delete'),
)
