from django.conf.urls import url
from type_one.forms import CustomAuthenticationForm

from . import views

urlpatterns=[
             url(r'^$', views.index, name='index'),
             url(r'^create/$', views.Create_failure.as_view(), name='create'),
             url(r'^confirm/$', views.confirm1, name='confirm1'),
             
             url(r'^list_failure/filtering/$', views.filtering, name='time'),
             url(r'^list_failure/(?P<pk>[0-9]+)/$', 
                 views.Failure_detail.as_view(), name='detail'),
             url(r'^list_failure/delete/(?P<pk>[0-9]+)/$', 
                 views.Delete_failure.as_view(), name='delete_failure'),
             
             url(r'^login/$', 'django.contrib.auth.views.login', 
                 {'authentication_form':CustomAuthenticationForm},name='login'),
             url(r'^logout/$', views.logout_page, name='logout'),
             url(r'^registration/$', 
                 views.registration_page, name='registration'),
             url(r'^account/(?P<user1>[\w]+)/$', views.account, name='account'),
             url(r'^(?P<slug>[\w]+)/detail/$', 
                 views.User_detail.as_view(), name='user_detail'),
             ]  
