from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^main/all', 'publication.views.mainAll'),
    url(r'^main/get/(?P<publication_id>\d+)/$', 'publication.views.mainCertain'),  
    url(r'^registration/', 'publication.views.registration'),
    url(r'^contacts/', 'publication.views.contacts'),
    url(r'^about/', 'publication.views.about'),
    url(r'^add/', include(admin.site.urls)),    
    url(r'^search/$', 'publication.views.search'),
)
