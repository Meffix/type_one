from django.conf.urls import url

from .forms import CustomAuthenticationForm

from . import views

urlpatterns=[
            url(r'^login/$', 'django.contrib.auth.views.login', 
                 {'authentication_form':CustomAuthenticationForm},name='login'),
            url(r'^logout/$', views.logout_page, name='logout'),
            url(r'^registration/$', 
                 views.registration_page, name='registration'),
            url(r'^account/(?P<user1>[\w]+)/$', views.account, name='account'),
            url(r'^(?P<slug>[\w]+)/detail/$', 
                 views.UserDetail.as_view(), name='user_detail'),
            ]