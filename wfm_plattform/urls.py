from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wfm_plattform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^tasks/',include('tasks.urls')),
    url(r'^agents/',include('agents.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profiles/',include('profiles.urls')),
    

)

if settings.DEBUG:
	urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
