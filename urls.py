from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('release.views',
    # Examples:
    # url(r'^$', 'releasourcer.views.home', name='home'),
    # url(r'^releasourcer/', include('releasourcer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^releases/$', 'index'),
    (r'^releases/(?P<release_id>\d+)/$', 'detail'),
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
)