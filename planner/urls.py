from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.login_page, name='login_page'),
    url(r'^sign_?up/?$',views.sign_up, name='sign_up'),
]
