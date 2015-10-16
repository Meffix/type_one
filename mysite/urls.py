from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views


urlpatterns = patterns('',
    url(r'^$', views.home_page, name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^type_one/',include('type_one.urls', namespace='type_one')),
)
