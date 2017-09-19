from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<ingredients>[0-9,]+)/$', views.search, name='search'),
    url(r'^recipy/(?P<recipy_id>[0-9]+)/$', views.recipy, name='recipy'),
]
