from django.urls import path, include
from django.conf.urls import url


from . import views

urlpatterns = [

	url(r'^color/(?P<value>\d+)/$', views.index, name='index')





]
