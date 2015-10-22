from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^type_one/',include('type_one.urls', namespace='type_one')),
    url(r'^list_failure/',include('view_failures.urls', namespace='view_failures')),
    url(r'^user/',include('accounts.urls', namespace='accounts')),
)
