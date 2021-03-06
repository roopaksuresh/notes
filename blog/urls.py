from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^note/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^note/new/$', views.post_new, name='post_new'),
    url(r'^note/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
