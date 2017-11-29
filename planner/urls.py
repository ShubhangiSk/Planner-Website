from django.conf.urls import url
from django.views.i18n import JavaScriptCatalog
from . import views
urlpatterns = [
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^$', views.login_page, name='login_page'),
    url(r'^sign_?up/?$',views.sign_up, name='sign_up'),
    url(r'^event/new/$', views.event_new, name='event_new'),
     url(r'^event/(?P<pk>\d+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^event/(?P<pk>\d+)/delete/$', views.event_delete, name='event_delete'),
    url(r'^event/(?P<pk>\d+)/$', views.event_detail, name='event_detail'),
    url(r'^official_events/?$',views.official_events, name='official_events'),
    url(r'^personal_events/?$',views.personal_events, name='personal_events'),
    url(r'^fun_events/?$',views.fun_events, name='fun_events'),
]
