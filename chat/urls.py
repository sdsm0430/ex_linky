# chat/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_list, name='main_list'),
    url(r'^main_detail/(?P<pk>\d+)/$', views.main_detail, name='main_detail'),
    url(r'^apply/(?P<pk>\d+)/$', views.apply, name='apply'),
    url(r'^apply_image/(?P<pk>\d+)/$', views.apply_image, name='apply_image'),
    url(r'^apply_complete/(?P<pk>\d+)/$', views.apply_complete, name='apply_complete'),
    url(r'^choice/(?P<pk>\d+)/$', views.choice, name='choice'),
    url(r'^review/(?P<pk>\d+)/$', views.review, name='review'),
    url(r'^user_korean/(?P<room_name>[^/]+)/$', views.user_korean, name='user_korean'),
    url(r'^user_japanese/(?P<room_name>[^/]+)/(?P<pk>\d+)/$', views.user_japanese, name='user_japanese'),
    url(r'^user_english/(?P<room_name>[^/]+)/(?P<pk>\d+)/$', views.user_english, name='user_english'),
    url(r'^user_chinese/(?P<room_name>[^/]+)/(?P<pk>\d+)/$', views.user_chinese, name='user_chinese'),
    url(r'^operate_list/$', views.operate_list, name='operate_list'),
    url(r'^operate_admin_password/(?P<pk>\d+)/$', views.admin_password, name='admin_password'),
    url(r'^operate_password/(?P<pk>\d+)/$', views.password, name='operate_password'),
    url(r'^operate/(?P<room_name>[^/]+)/$', views.operate, name='operate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)