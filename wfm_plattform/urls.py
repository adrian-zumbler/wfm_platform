from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wfm_plattform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^tasks/',include('tasks.urls')),
    url(r'^admin/', include(admin.site.urls)),
    

)