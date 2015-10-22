from django.conf.urls import url
#from type_one.forms import CustomAuthenticationForm

from . import views

urlpatterns=[
             url(r'^$', views.index, name='index'),
             url(r'^create/$', views.CreateFailure.as_view(), name='create'),
             url(r'^confirm/$', views.confirm1, name='confirm1'),
             ]  
