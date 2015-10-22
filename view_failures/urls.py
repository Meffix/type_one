from django.conf.urls import url
from . import views

urlpatterns =[
              url(r'^filtering/$', views.filtering, name='time'),
              url(r'^(?P<pk>[0-9]+)/$', 
                  views.FailureDetail.as_view(), name='detail'),
              url(r'^delete/(?P<pk>[0-9]+)/$', 
                 views.DeleteFailure.as_view(), name='delete_failure'),
              ]