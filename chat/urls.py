# chat/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^choice/$', views.choice, name='choice'),
    url(r'^review/$', views.review, name='review'),
    url(r'^chat/$', views.index, name='index'),
    url(r'^chat/user_korean$', views.user_korean, name='user_korean'),
    url(r'^chat/user_japanese$', views.user_japanese, name='user_japanese'),
    url(r'^chat/user_english$', views.user_english, name='user_english'),
    url(r'^chat/user_chinese$', views.user_chinese, name='user_chinese'),
    url(r'^chat/(?P<room_name>[^/]+)/$', views.room, name='room'),
]