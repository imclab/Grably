from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from app import views
from foursq_auth import views
from django.contrib import admin #HP uncommented
admin.autodiscover() #HP uncommented

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog', {}, ""),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')), #HP uncommented
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)), #HP uncommented
    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), #HP
    (r'^foursq_auth/', include('grably.foursq_auth.urls')),
)
