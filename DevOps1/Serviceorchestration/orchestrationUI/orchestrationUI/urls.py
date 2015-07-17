from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  
    url(r'^$', 'orchestrationUI.views.my_view', name='home'),
    url(r'vnfd$', 'orchestrationUI.views.my_view1', name='home'),
    #commented for test purpose
    url(r'vld$', 'orchestrationUI.views.my_view2', name='home'),
    url(r'vnffgd$', 'orchestrationUI.views.my_view3', name='home'),
    url(r'nsd$', 'orchestrationUI.views.my_view4', name='home'),
    #end comment
    url(r'work$', 'orchestrationUI.views._work', name='home'),
    url(r'onboard$', 'orchestrationUI.views.my_view5', name='home'),
    url(r'createVNF$', 'orchestrationUI.views.create_vnf', name='home'),
    url(r'^home$', 'orchestrationUI.views.my_view', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
