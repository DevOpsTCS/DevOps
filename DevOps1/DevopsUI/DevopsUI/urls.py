from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'DevopsUI.views.my_view', name='home'),
    url(r'vnfd$', 'DevopsUI.views.my_view1', name='home'),
    url(r'vld$', 'DevopsUI.views.my_view2', name='home'),
    #url(r'vnffgd$', 'DevopsUI.views.my_view3', name='home'),
    url(r'nsd$', 'DevopsUI.views.my_view4', name='home'),
    url(r'onboard$', 'DevopsUI.views.my_view5', name='home'),
    url(r'createVNF$', 'DevopsUI.views.create_vnf', name='home'),
    #createVNF
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
