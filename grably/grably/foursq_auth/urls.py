from django.conf.urls.defaults import *
from foursq_auth.views import *

urlpatterns = patterns('foursq_auth.views',
    # main page redirects to start or login
    url(r'^$', view=main, name='main'),
    # receive OAuth token from 4sq
    url(r'^callback/$', view=callback, name='oauth_return'),
    # logout from the app
    url(r'^logout/$', view=unauth, name='oauth_unauth'),
    # authenticate with 4sq using OAuth
    url(r'^auth/$', view=auth, name='oauth_auth'),
    # main page once logged in
    url( r'^done/$', view=done, name='oauth_done' ),
    url(r'^tasks/$', view=edit_form, name='edit_tasks'),
    url(r'^_add_task/$', view=create_task, name='add_task'),
    url(r'^twitter/$', view=twitter, name='get twitter handle'),
    url(r'^process/$', view=twitter_handle)
)
