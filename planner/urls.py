from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.login_page, name='login_page'),
    url(r'^sign_?up/?$',views.sign_up, name='sign_up'),
    url(r'^event/new/$', views.event_new, name='event_new'),
     url(r'^event/(?P<pk>\d+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^event/(?P<pk>\d+)/$', views.event_detail, name='event_detail'),
]
